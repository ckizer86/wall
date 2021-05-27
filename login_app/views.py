from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from time import gmtime, localtime, strftime
from datetime import date, datetime
from .models import *

# Create your views here.

def index(request):
    if "user_id" in request.session:
        return redirect ('wall_app:wall_index')

    return render(request, "loginindex.html")

def success(request):
    if "user_id" not in request.session:
        return redirect ('login_app:login_index')

    return render(request, "success.html")

def register(request):
    if request.method == "POST":

        errors = User.objects.uservalidation(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request,error)
            return redirect('login_app:login_index')

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        dob = request.POST["dob"]
        email = request.POST["email"]
        password = bcrypt.hashpw(request.POST["pw"].encode(), bcrypt.gensalt()).decode()

        user = User.objects.create(first_name=first_name, last_name=last_name, dob=dob, email=email, pw=password)
        request.session["user_id"] = user.id
        request.session["username"] = f"{user.first_name} {user.last_name}"
        return redirect('wall_app:wall_index')
    return redirect('login_app:login_index')

def login(request):
    if request.method == "POST":
        email = request.POST["email"]

        logged_user = User.objects.filter(email=email)
        if logged_user:
            logged_user = logged_user[0]
            if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.pw.encode()):
                request.session["user_id"] = logged_user.id
                request.session["username"] = f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('wall_app:wall_index')
            else:
                messages.error(request, "Invalid password")
                return redirect('login_app:login_index')
        else:
            messages.error(request, "Invalid email")
            return redirect ('login_app:login_index')

    return redirect('login_app:login_index')

def logout(request):
    request.session.flush()

    return redirect('login_app:login_index')