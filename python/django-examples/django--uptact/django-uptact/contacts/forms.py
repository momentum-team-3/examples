from django import forms
from .models import Contact, Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'text',
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'birthdate',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
        ]
