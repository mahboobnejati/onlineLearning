from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField('email address', unique=True, db_index=True)
    first_name = models.CharField(default="unknown", max_length=30)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

'''class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    avatar = models.ImageField(upload_to = '/images/', null = True, blank = True, max_length = 250)
    group_join = models.ForeignKey(Group)
    course_in = models.ForeignKey(Course)
    score = models.IntegerField()

class Group(models.Model):

class Course(models.Model):'''



class Student(User):
    name = models.CharField(max_length=30)
    #credit = models.IntegerField()
    #score = models.IntegerField()

class Exam(models.Model):
    name = models.CharField(max_length=30)
    #num_Question = models.IntegerField()
    #time = models.TimeField(auto_now=False)

class TotalExam(Exam):
    #date = models.DateField()
    start_time = models.TimeField(auto_now=False)

class Ques_Ans(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    #answer = models.IntegerField()

class Ans(models.Model):
    ques_ans = models.ForeignKey(Ques_Ans,on_delete=models.CASCADE)


