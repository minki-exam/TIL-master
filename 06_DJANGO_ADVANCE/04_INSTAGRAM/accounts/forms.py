from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email',)


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User