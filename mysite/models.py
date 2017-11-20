from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.db.models.fields import IntegerField

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.template.defaultfilters import default

class EmailRequiredMixin(object):
    def __init__(self, *args, **kwargs):
        super(EmailRequiredMixin, self).__init__(*args, **kwargs)
        # make user email field required
        self.fields['email'].required = True
        
class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
    pass


class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
    pass

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=32, blank=False)
    no_of_mentors = IntegerField()
    no_of_student = IntegerField()#Student.objects.filter(mentor_id = user.id).count()
    
    def __str__(self):
        return str(self.user) 
    
    class Meta:
        ordering = ('user',)
    
    def __unicode__(self):
        return self.emp_id

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    no_of_students = IntegerField() #Student.objects.filter(mentor_id = user.id).count()
    
    def __str__(self):
        return str(self.user.name)

class Student(models.Model):
    name = models.CharField(max_length = 50)
    school = models.CharField(max_length = 50)
    address = models.TextField(blank=True)
    contact_no = models.IntegerField(blank=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    mentor = models.OneToOneField(Mentor, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.first_name) 
    
    class Meta:
        ordering = ('id',) 
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    subject = models.CharField(max_length=20)
    date = models.DateField(blank=True)
    
    ATTENDANCE_CHOICES = (
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LATE', 'Late'),
    ) 
    attendance = models.CharField(max_length=5,choices=ATTENDANCE_CHOICES,default=None)
    
    def __str__(self):
        return str(self.user.name)
    
class Appointment(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default = None, blank=True)
    
    def __str__(self):
        return str(self.date)
  
class PersonalInfo(models.Model):
    user = models.OneToOneField(User)
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    )
    
    gender = models.CharField(max_length=5,choices=GENDER_CHOICES,default=None)
    contact_info = models.IntegerField() 
    address = models.TextField(max_length=200)
    
    def __str__(self):
        return str(self.id) 
    
    class Meta:
        ordering = ('id',)
        
        
class Role(models.Model):
    name = models.CharField(max_length=30, blank=False)
    desc = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return str(self.name) 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.OneToOneField(Role, on_delete=models.CASCADE)

class ProfileInline(admin.TabularInline):
    model = Profile
    fk_name = 'user'
    
class PersonalInfoInline(admin.TabularInline):
    model = PersonalInfo
    fk_name = 'user'
    
class CustomUser(UserAdmin):
    #exclude = ('username',)
    fieldsets = (
        ('Personal info', {'fields': ( 'email','password')}),
    )
    
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    add_fieldsets = ((None, {'fields': ('username', 'email',
                                        'password1', 'password2'), 'classes': ('wide',)}),)


    inlines = [
        PersonalInfoInline, ProfileInline 
    ]
    
    def __str__(self):
        return str(self.id) 
    
    class Meta:
        ordering = ('id',)
    
    
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Role)
admin.site.register(Appointment)

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, CustomUser)
