from django.db import models

# Create your models here.

class NoteModel(models.Model):
    note_title = models.CharField(max_length=200, null=False,blank=False)
    note_description= models.TextField(max_length=255, null=False,blank=False)

    def __str__(self):
        return self.note_title +self.note_description


    class Meta:
        db_table='tbl_notes'



