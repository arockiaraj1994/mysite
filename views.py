from django.http import HttpResponse
from . import serializers
from . import models
from . import forms
from django.shortcuts import render
from django.template import loader, RequestContext


def status(request):
    return HttpResponse(status=201)

def tem(request):
    import pdb;pdb.set_trace()
    form = forms.StudentForm()
    return render(request, 'student.html', {'form': form})