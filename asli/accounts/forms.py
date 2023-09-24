from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *
from content.models import Twit

class UserCrationForm(forms.ModelForm):
    password=forms.CharField()
    password2=forms.CharField()

    class Meta:
        model=User
        fields=('email','username')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
            raise ValidationError('Passwords is not Mach')
        return cd['password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()

    class Meta:
        model=User
        fields=('email','username','password','last_login')



# Authenticated User...
class UserLoginForm(forms.Form):
    email = forms.CharField(label='email',widget=forms.TextInput)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

# Authenticated User...
class UserSinginForm(forms.Form):
    email = forms.CharField(label='email',widget=forms.TextInput)
    username = forms.CharField(label='username',widget=forms.TextInput)
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email = email).exists()
        if user:
            print('=======================OK==========================')
            raise ValidationError('Email is alredy...')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username = username).exists()
        if user:
            print('=======================OK==========================')
            raise ValidationError('Username is alredy...')
        return username
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
            print('=======================OK==========================')
            raise ValidationError('Passwords is Not Match...')
        return cd['password2']
    
# Form Profile Users...
class UpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}))
    bio = forms.CharField(label='bio',widget=forms.TextInput(attrs={'class':'form-control'}))
    img = forms.ImageField(label='img',widget=forms.FileInput)

    class Meta:
        model = User
        fields = ('email','username','bio','img')

    

    


    

