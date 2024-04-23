from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout


def home(request):
	if request.user.is_authenticated:
		return render(request, 'main/home.html')
	return HttpResponseRedirect('/login')


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
