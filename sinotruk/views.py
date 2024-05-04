from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.http import FileResponse, JsonResponse
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import IP2Location


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
				return HttpResponseRedirect('/')

		else:
			return render(request, 'main/login.html')


def logout_view(request):
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
		user.delete()

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
			user.set_password(password)
			user.save()

			return HttpResponseRedirect('/managers')

		else:
			return render(request, 'main/add_manager.html')
	else:
		return HttpResponseRedirect('/')


def dealers(request):
	managers = CustomUser.objects.filter(role='DEALER')

	return render(request, 'main/dealers.html', {
		'dealers': managers,
		'dealers_count': managers.count(),
	})


def add_dealer(request):
	if request.user.role == 'ADMIN':
		if request.method == 'POST':

			username = request.POST.get('username')
			password = request.POST.get('password')

			user = CustomUser.objects.create_user(username=username, password=password, role='DEALER')
			user.set_password(password)
			user.save()

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

			Activity.objects.create(
				user=request.user,
				ip=request.META['REMOTE_ADDR'],
				action=f'Загрузка файла "{file.title}"'
			)

			return HttpResponseRedirect('/files/' + str(file.id))
	else:
		return render(request, 'main/add_file.html', {'form': AddFileForm()})


def get_document(request, doc_id):
	file = Document.objects.get(id=doc_id)

	Activity.objects.create(
		user=request.user,
		ip=request.META['REMOTE_ADDR'],
		action=f'Скачивание файла "{file.title}"'
	)

	return FileResponse(file.document)


def activity(request):
	return render(request, 'main/activity.html')
