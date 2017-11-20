from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from mysite.models import PersonalInfo, Profile
#from mysite.models import CustomUser


class UserForm(ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )
            
class PersonalForm(ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ( 'gender', 'contact_info','address')
        widgets = {
            'gender': forms.TextInput(attrs={'style': 'background-color:powderblue;'}),
        }
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name',)
        
class StudentForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    
