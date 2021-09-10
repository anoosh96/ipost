from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from forms.mixins import FormControlMixin
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm,FormControlMixin):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)
        self.add_form_control_class()

    class Meta:
        model=User
        fields=['email','password1','password2']
    


class LoginUserForm(AuthenticationForm, FormControlMixin):
    def __init__(self, *args, **kwargs):
        super(LoginUserForm,self).__init__(*args, **kwargs)
        self.add_form_control_class()

    class Meta:
        model=User
        fields=['email','password']

