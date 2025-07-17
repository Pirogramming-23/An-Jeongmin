from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path("",idea_list, name="idea_list"),
    path("create/",idea_create, name="idea_create"),
    path("detail/<int:pk>/",idea_detail, name="idea_detail"),
    path("update/<int:pk>/",idea_update, name="idea_update"),
    path("delete/<int:pk>/",idea_delete, name="idea_delete"),
    path('<int:pk>/update_interest/', update_interest, name='update_interest'),
    path('<int:pk>/star/', star_idea, name='star'),
    path('<int:pk>/unstar/', unstar_idea, name='unstar'),
]