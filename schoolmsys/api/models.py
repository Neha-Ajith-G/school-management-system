
# Create your models here.
#User-Model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username


class Student(models.Model):
  student_number = models.PositiveIntegerField(primary_key=True)
  student_name = models.CharField(max_length=50)

  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  

  def __str__(self):
    return f'Student: {self.student_name}'



class Subject(models.Model):
    subject_number = models.PositiveIntegerField()
    subject_name = models.CharField(max_length=50)
    teacher = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, limit_choices_to={'role': 'teacher'})
    class Meta:
        unique_together = ['subject_number', 'subject_name']

    def __str__(self):
        return f'Subject: {self.subject_name}'


class Mark(models.Model):
    student_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
      unique_together = ['student_number', 'subject_name']
    def __str__(self):
        return f'Mark: {self.student_number}>>{self.subject_name};{self.marks_obtained}'