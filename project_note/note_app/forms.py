from django import forms
from note_app.models import NoteModel

class noteForm(forms.ModelForm):
    class Meta:
        # fields = ("__all__") # for all fields
        fields = ("note_title","note_description","status")
        model= NoteModel