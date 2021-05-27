from django.urls import path
from . import views
app_name='wall_app'

urlpatterns=[
    path('', views.index, name='wall_index'),
    path('/post_message', views.post_message, name='post_message'),
    path('/post_comment', views.post_comment, name='post_comment'),
    path('/destroy_comment/<int:id>', views.destroy_comment, name="wall_destroy_comment"),
    path('/destroy_message/<int:id>', views.destroy_message, name="wall_destroy_message"),
]