from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    
