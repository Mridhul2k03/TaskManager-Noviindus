from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'completion_report', 'worked_hours', 'status']
        read_only_fields = ['id', 'completion_report', 'worked_hours', 'status']