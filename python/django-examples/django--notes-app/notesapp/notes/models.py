from django.db.models import Model, CharField, TextField, DateTimeField

# Create your models here.
class Note(Model):
    note_title = CharField(max_length=200, null=False, blank=False)
    note_body = TextField(null=False, blank=False)
    date_created = DateTimeField(auto_now_add=True)

