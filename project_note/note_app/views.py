from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'notes/index.html')

def create_note(request):
    return render(request,'notes/createNote.html')