from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Course(models.Model):
	crn = models.CharField(primary_key = True, max_length = 5, validators=[RegexValidator(regex='^[0-9]{5}$', message='Length has to be 5, and it should not contain any character', code='nomatch')])
	available = models.IntegerField(default = 0, null = False)

class Watch(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_column='user')
	crn = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, db_column='crn')

