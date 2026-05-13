from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_note/", views.create, name="create_note"),
]
