from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        #can work even without below line as UserCreationForm intends User database but in complex codes to conform that desired database is reffered
        model=User 
        #below line used to order the fields of form
        fields=['username','email','password1','password2']
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta: 
        model=User 
        fields=['username','email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile 
        fields=['image']