from django.contrib.auth.forms import UserCreationForm
from .models import User


class ContactUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
