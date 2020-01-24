from django import forms
from .models import Profile,Image,Comment,Gari
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30, required=False, help_text='Optional.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    Bio=forms.CharField(max_length=70, required=False, help_text='Optional.')
    name=forms.CharField(max_length=30, required=False, help_text='Optional.')
    profile_image=forms.ImageField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','Bio','name','profile_image','email', 'password1', 'password2', )
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('first_name','last_name','email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'Bio', 'profile_image']  
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')              
class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields = ['name','image_caption','image_path']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['comment']


# class NewGariForm(forms.ModelForm):
#     class Meta:
#         model = Gari
#         exclude = ['user','profile','pub_date']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }
        
class NewUsedForm(forms.ModelForm):
    class Meta:
        model = Gari
        exclude = ['user','profile','pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
            
        
class NewCarForm(forms.ModelForm):
    class Meta:
        model = Gari
        exclude = ['user','profile','pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }                