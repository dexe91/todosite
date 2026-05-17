from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_note/", views.create_note, name="create_note"),
    path("note/<int:note_id>/toggle/", views.toggle_note, name="toggle_note"),
]
