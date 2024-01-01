from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('createNote/',views.create_note,name="create-note"),
    path('addNote/', views.AddNote, name="add-note"),
    path('update/<int:id>',views.update_notes,name='update'),
    path('updateData/', views.updateData, name='update_data'),
]
