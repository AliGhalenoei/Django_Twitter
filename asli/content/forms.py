from django import forms
from .models import *


class CommentTwitForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = CommentTwit
        fields =('comment',)

class UpdateCommentTwitForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = CommentTwit
        fields =('comment',)

class TwitForm(forms.ModelForm):
    #img = forms.ImageField(widget=forms.FileField)
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Twit
        fields =('img','description')

class UpdateTwitForm(forms.ModelForm):
    #img = forms.ImageField(label='img',widget=forms.FileField)
    img = forms.ImageField(label='img',widget=forms.FileInput)

    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Twit
        fields =('img','description')

    


