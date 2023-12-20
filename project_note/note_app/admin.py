from django.contrib import admin
from .models import NoteModel

# Register your models here.
class NoteAdminModel(admin.ModelAdmin):
    list_display=("note_title","note_description")


admin.site.register(NoteModel,NoteAdminModel)
