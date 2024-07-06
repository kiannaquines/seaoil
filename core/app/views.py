from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from app.decorators import check_already_loggedin

@login_required(login_url="auth/login/")
def index(request):
	return render(request,"index.html")

@check_already_loggedin
def auth_login(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		login_action = CustomUser.objects.filter(username=username)

		if login_action.exists():

			if login_action[0].is_active is not True:
				messages.error(request,"Your account is not activated yet, wait while we process your account activation.")
				return HttpResponseRedirect('/auth/login/')
			else:
				auth = authenticate(request,username=username,password=password)
			
			if auth is not None:
				login(request,auth)
				messages.success(request,"You have successfully logged in.")
				return HttpResponseRedirect('/')
			else:
				messages.error(request,"Incorrect username/password, please try again.")
				return render(request,"auth/login.html")
		else:
			messages.error(request,"We cannot find your account, please try again.")
			return render(request,"auth/login.html")
		
	return render(request,"auth/login.html")


def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/auth/login')

@check_already_loggedin
def auth_register(request):
	if request.method == "POST":
		username = request.POST.get("username")
		first_name = request.POST.get("firstname")
		last_name = request.POST.get("lastname")
		password = make_password(request.POST.get("password"))


		if CustomUser.objects.filter(username=username).exists():
			messages.error(request,"Sorry, username already exist, please try again.")
			return render(request,"auth/register.html")
		
		CustomUser.objects.create(username=username,first_name=first_name,last_name=last_name,password=password,is_active=False)
		messages.success(request,"You have successfully registered, please wait to activate your account.")
		return HttpResponseRedirect("/auth/login")

	return render(request,"auth/register.html")

@login_required(login_url="auth/login/")
def user_profile(request,pk):
	context = {}
	if request.method == "GET":
		user = CustomUser.objects.get(pk=pk)
		context["user"] = user
		return render(request,"auth/profile.html",context)
	
@login_required(login_url="auth/login/")
def user_update(request,pk):
	pass

