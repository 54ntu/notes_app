from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('createNote/',views.create_note,name="create-note"),
    path('addNote/', views.AddNote, name="add-note"),
]
