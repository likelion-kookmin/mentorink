from django.contrib.auth.forms import UserCreationForm
from .models import UserModel


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1',
                  'password2', 'nickname', 'position', ]
