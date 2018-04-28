from rest_framework import serializers

from app.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('crn', 'available')

class WatchSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    crn = CourseSerializer(required=True)
    class Meta:
        model = Watch
        fields = ('user', 'crn')