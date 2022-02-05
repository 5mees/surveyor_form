from django.forms import ModelForm
from .models import StudentData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(ModelForm):
    class Meta:
        model = StudentData
        fields = '__all__'


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
