from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from time import gmtime, localtime, strftime
from datetime import date, datetime
from .models import *

# Create your views here.
def index(request):
    if "user_id" not in request.session:
        return redirect('login_app:login_index')
    context = {
        "messages": Message.objects.all(),
    }
    
    return render(request, "index.html", context)

def post_message(request):
    if request.method == "POST":
        message = request.POST["message"]
        userid = request.session['user_id']
        user = User.objects.get(id=userid)
        Message.objects.create(poster = user, message=message)

        return redirect('wall_app:wall_index')
    return redirect('login_app:login_index')

def post_comment(request):
    if request.method == "POST":
        comment = request.POST["comment"]
        messageid = request.POST["messagepost"]
        userid = request.session['user_id']
        user = User.objects.get(id=userid)
        message = Message.objects.get(id=messageid)
        Comment.objects.create(commenter = user, message = message, comment = comment)

        return redirect('wall_app:wall_index')
    return redirect('login_app:login_index')

def destroy_comment(request, id):
    commentid = id
    comment = Comment.objects.get(id=commentid)
    if request.session['user_id'] == comment.commenter.id:
        comment.delete()
        return redirect('wall_app:wall_index')
    return redirect('wall_app:wall_index')

def destroy_message(request, id):
    messageid = id
    message = Message.objects.get(id=messageid)
    if request.session['user_id'] == message.poster.id:
        message.delete()
        return redirect('wall_app:wall_index')
    return redirect('wall_app:wall_index')