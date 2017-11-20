from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models.fields import IntegerField


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=32, blank=False)
    no_of_mentors = IntegerField()
    no_of_student = IntegerField()#Student.objects.filter(mentor_id = user.id).count()
    
    
    def __str__(self):
        return str(self.first_name) 
    
    class Meta:
        ordering = ('user',)
        

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
    student = models.ForeignKey(Student, models.CASCADE)
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
    
    def __str__(self):
        return str(self.subject)

#class Appointment(models.Model):
    
  
class PersonalInfo(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
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
    
class UserAdmin(UserAdmin):
    #exclude = ('username',)
    actions = ['delete_selected']
    fieldsets = (
        ('Personal info', {'fields': ( 'email',)}),
    )

    inlines = [
        PersonalInfoInline, ProfileInline 
    ]
    
    
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Employee)
admin.site.register(Attendance)
#admin.site.register(PersonalInfo)
admin.site.register(Role)
#admin.site.register(Profile)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
