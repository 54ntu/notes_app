from django.shortcuts import render,redirect
from .models import NoteModel
from note_app.forms import noteForm

# Create your views here.

def index(request):
    notes= NoteModel.objects.all() #here we fetch all the data from database where NoteModel is Model name and storing in notes variablex
    context={
        "note":notes,
    }
    
    
    return render(request,'notes/index.html',context)



def create_note(request):
    return render(request,'notes/createNote.html')

def AddNote(request):
    if request.method=="POST":
        obj= NoteModel()
        obj.note_title=request.POST.get('note_title')
        obj.note_description= request.POST.get('note_desc')
        obj.save()
        return redirect('index')
    return redirect('create-note')


def update_notes(request,id):
    note= NoteModel.objects.get(id=id)
    context={
        "note":note,
    }
    return render(request,'notes/updatePage.html',context)

def updateData(request):
   if request.method == "POST":
       instance = NoteModel.objects.get(id=request.POST.get("id"))
       data = noteForm(data= request.POST, instance=instance)
       print("data : ", data)
       if data.is_valid():
           data.save()
           return redirect('index')
       return redirect('update')
