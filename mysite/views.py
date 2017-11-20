from django.http import HttpResponse
from . import forms
from django.shortcuts import render
from django.template import loader, RequestContext
from mysite.forms import UserForm, PersonalForm, ProfileForm
from mysite.models import Employee
from mysite.tables import EmployeeTable


def status(request):
    return HttpResponse(status=201)

def tem(request):
    form = forms.StudentForm()
    return render(request, 'student.html', {'form': form})

def create_user(request):
    if request.method == "POST":
        #import pdb;pdb.set_trace()
        form = UserForm(request.POST)
        personal_form = ProfileForm(request.POST)
        if form.is_valid():
            #new_user = User.objects.create_user(**form.cleaned_data)
            #login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('user.html')
    else:
        form = UserForm()
        
    personal_form = PersonalForm()
    profile_form = ProfileForm()
    return render(request, 'user.html', {'form': form, 'form1':personal_form, 'form2':profile_form})

def emp_list(request):
    emp = EmployeeTable()     
    return render(request, "emp_list.html", {'emp': emp})
    