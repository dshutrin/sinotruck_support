from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.http import FileResponse, JsonResponse
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import IP2Location


def ip_info(addr):
	from urllib.request import urlopen
	from json import load
	url = 'https://ipinfo.io/' + addr + '/json'
	res = urlopen(url)
	data = load(res)

	if 'city' in data.keys():
		return "Place: " + data['city'] + " " + data['region'] + " " + data['loc']
	elif addr == '127.0.0.1':
		return 'SERVER (LOCAL)'
	else:
		return 'not found'


def login_view(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:

		if request.method == 'POST':

			login = request.POST.get('login')
			password = request.POST.get('password')

			usr = authenticate(request, username=login, password=password)
			if usr is not None:
				user_login(request, usr)
				Activity.objects.create(
					user=usr,
					action='Авторизация',
					ip=request.META['REMOTE_ADDR'],
					place=ip_info(request.META['REMOTE_ADDR'])
				)
				return HttpResponseRedirect('/')

		else:
			return render(request, 'main/login.html')


def logout_view(request):
	Activity.objects.create(
		user=request.user,
		action='Выход из аккаунта',
		ip=request.META['REMOTE_ADDR'],
		place=ip_info(request.META['REMOTE_ADDR'])
	)
	user_logout(request)
	return HttpResponseRedirect('/login')


def home(request):
	if request.user.is_authenticated:
		return render(request, 'main/home.html', {
			'managers_count': CustomUser.objects.filter(role='MANAGER').count(),
			'dealers_count': CustomUser.objects.filter(role='DEALER').count(),
			'clients_count': CustomUser.objects.filter(role='CLIENT').count()
		})
	return HttpResponseRedirect('/login')


@csrf_exempt
def get_user_details(request, user_id):
	if request.user.is_authenticated:
		user = CustomUser.objects.get(id=user_id)

		return JsonResponse({
			'username': user.username,
		}, status=200)


@csrf_exempt
def delete_user(request, user_id):
	if request.user.is_authenticated:
		user = CustomUser.objects.get(id=user_id)
		user_name = user.username
		user.delete()

		Activity.objects.create(
			user=request.user,
			action=f'Удаление пользователя {user_name}',
			ip=request.META['REMOTE_ADDR'],
			place=ip_info(request.META['REMOTE_ADDR'])
		)

		return JsonResponse({}, status=200)


def managers(request):
	managers = CustomUser.objects.filter(role='MANAGER')

	return render(request, 'main/managers.html', {
		'managers': managers,
		'manager_count': managers.count(),
	})


def add_manager(request):
	if request.user.role == 'ADMIN':
		if request.method == 'POST':

			username = request.POST.get('username')
			password = request.POST.get('password')
			name = request.POST.get('name')
			surname = request.POST.get('surname')

			user = CustomUser.objects.create_user(username=username, password=password, name=name, surname=surname, role='MANAGER')
			user.custom_set_password(password)
			user.save()

			Activity.objects.create(
				user=request.user,
				action=f'Добавление менеджера {user.username}',
				ip=request.META['REMOTE_ADDR'],
				place=ip_info(request.META['REMOTE_ADDR'])
			)

			return HttpResponseRedirect('/managers')

		else:
			return render(request, 'main/add_manager.html')
	else:
		return HttpResponseRedirect('/')


def dealers(request):
	managers = CustomUser.objects.filter(role='DILER')

	return render(request, 'main/dealers.html', {
		'dealers': managers,
		'dealers_count': managers.count(),
	})


def add_dealer(request):
	if request.user.role == 'ADMIN':
		if request.method == 'POST':

			username = request.POST.get('username')
			password = request.POST.get('password')
			firm = request.POST.get('firm')

			user = CustomUser.objects.create_user(username=username, password=password, role='DEALER', dealer_name=firm)
			user.custom_set_password(password)
			user.save()

			Activity.objects.create(
				user=request.user,
				action=f'Добавление дилера {user.username}',
				ip=request.META['REMOTE_ADDR'],
				place=ip_info(request.META['REMOTE_ADDR'])
			)

			return HttpResponseRedirect('/dealers')

		else:
			return render(request, 'main/add_dealer.html')
	else:
		return HttpResponseRedirect('/')


def clients(request):
	return render(request, 'main/clients.html')


def pricelist(request):
	return render(request, 'main/pricelist.html')


def files(request):
	files = Document.objects.all()

	return render(request, 'main/files.html', {
		'files': files,
		'files_count': files.count()
	})


def add_file(request):
	if request.method == 'POST':

		form = AddFileForm(request.POST, request.FILES)
		if form.is_valid():
			file = form.save()
			if file.document.path.endswith('.pdf'):
				file.file_type = 'pdf'
			if file.document.path.endswith('.doc'):
				file.file_type = 'doc'
			if file.document.path.endswith('.docx'):
				file.file_type = 'doc'
			if file.document.path.endswith('.xlsx'):
				file.file_type = 'xlsx'
			if file.document.path.split('.')[-1] in ['jpg', 'jpeg', 'png', 'gif']:
				file.file_type = 'image'

			file.save()

			Activity.objects.create(
				user=request.user,
				ip=request.META['REMOTE_ADDR'],
				action=f'Загрузка файла "{file.title}"',
				place=ip_info(request.META['REMOTE_ADDR'])
			)

			return HttpResponseRedirect('/files/' + str(file.id))
	else:
		return render(request, 'main/add_file.html', {'form': AddFileForm()})


def get_document(request, doc_id):
	file = Document.objects.get(id=doc_id)

	Activity.objects.create(
		user=request.user,
		ip=request.META['REMOTE_ADDR'],
		action=f'Скачивание файла "{file.title}"',
		place=ip_info(request.META['REMOTE_ADDR'])
	)

	return FileResponse(file.document)


def activity(request):
	return render(request, 'main/activity.html')


def edit_user(request, user_id):
	user = CustomUser.objects.get(id=user_id)

	if request.method == 'GET':
		if user.role == 'MANAGER':
			form = EditManagerForm(instance=user)
			return render(request, 'main/edit_user.html', {'user': user, 'form': form})
		elif user.role == 'DILER':
			form = EditDealerForm(instance=user)
			return render(request, 'main/edit_user.html', {'user': user, 'form': form})
		else:
			return HttpResponseRedirect('/')

	elif request.method == 'POST':

		Activity.objects.create(
			user=request.user,
			action=f'Изменение данных пользователя {user.username}',
			ip=request.META['REMOTE_ADDR'],
			place=ip_info(request.META['REMOTE_ADDR'])
		)

		if user.role == 'MANAGER':
			form = EditManagerForm(instance=user, data=request.POST)

			if form.is_valid():

				user.username = form.cleaned_data['username']
				user.name = form.cleaned_data['name']
				user.surname = form.cleaned_data['surname']
				user.role = form.cleaned_data['role']
				user.sub_role = form.cleaned_data['sub_role']
				user.custom_set_password(form.cleaned_data['clear_password'])

				return HttpResponseRedirect('/managers')

			else:
				return render(request, 'main/edit_user.html', {'user': user, 'form': form})

		elif user.role == 'DILER':
			form = EditDealerForm(instance=user, data=request.POST)

			if form.is_valid():

				user.username = form.cleaned_data['username']
				user.name = form.cleaned_data['name']
				user.surname = form.cleaned_data['surname']
				user.role = form.cleaned_data['role']
				user.dealer_name = form.cleaned_data['dealer_name']
				user.custom_set_password(form.cleaned_data['clear_password'])

				return HttpResponseRedirect('/dealers')

			else:
				return render(request, 'main/edit_user.html', {'user': user, 'form': form})

		else:
			return HttpResponseRedirect('/')
