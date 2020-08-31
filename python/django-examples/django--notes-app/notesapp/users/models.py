import django.contrib.auth as dj_auth
# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(dj_auth.models.AbstractUser):
    pass
