from django.db import models
from login_app.models import *
# Create your models here.

class Message(models.Model):
    poster = models.ForeignKey(User, related_name="user", on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # msgcomment
    # commentuser

class Comment(models.Model):
    commenter = models.ForeignKey(User, related_name="commentuser", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="msgcomment", on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

