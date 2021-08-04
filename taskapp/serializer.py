from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import  Task, Register


class TaskSerializser(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['Title','Description','TaskStatus','TaskID']

