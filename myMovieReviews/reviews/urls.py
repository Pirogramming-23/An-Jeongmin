from django.urls import path
from .views import *

urlpatterns = [
    path('', review_list, name='review_list'),
    path("<int:pk>/", review_detail, name='review_detail'),
    path("create/", review_create, name='review_create'),
    path("<int:pk>/update/", review_update, name='review_update'),
    path("<int:pk>/delete/",review_delete, name='review_delete'),
]