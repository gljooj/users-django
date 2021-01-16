from django.contrib.auth.models import User
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']
        help_texts = {
            'username': None,
            'email': None,
            'is_active': None
        }
