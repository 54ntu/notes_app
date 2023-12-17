from django.urls import path
from . import views

urlpatterns = [
    path('noteList/',views.index,name="index"),
    
]
