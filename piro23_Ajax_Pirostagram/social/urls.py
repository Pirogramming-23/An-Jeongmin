from django.urls import path
from .views import *

urlpatterns = [
    path("",home, name = "home"),
    path("like/<int:post_id>", like_post, name = "like_post"),
    path("comment/<int:post_id>/add/", add_comment, name ="add_comment"),
    path("comment/<int:post_id>/delete/", delete_comment, name ="delete_comment"),
]