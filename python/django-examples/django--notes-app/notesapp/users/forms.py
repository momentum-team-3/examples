import django.contrib.auth as dj_auth
from .models import User


class UserCreationForm(dj_auth.forms.UserCreationForm):
    class Meta(dj_auth.forms.UserCreationForm.Meta):
        model = User
        fields = dj_auth.forms.UserCreationForm.Meta.fields

        
class UserChangeForm(dj_auth.forms.UserChangeForm):
    class Meta(dj_auth.forms.UserChangeForm.Meta):
        model = User
        fields = dj_auth.forms.UserChangeForm.Meta.fields


class AuthenticationForm(dj_auth.forms.AuthenticationForm):
    pass


class PasswordResetForm(dj_auth.forms.PasswordResetForm):
    pass

class SetPasswordForm(dj_auth.forms.SetPasswordForm):
    pass


class PasswordChangeForm(dj_auth.forms.PasswordChangeForm):
    pass
