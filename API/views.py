from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .permissions import IsAdminUser, IsSuperAdminUser, IsUser, IsAdminOrSuperAdmin

# Create your views here.


class TaskAPIView(APIView):
    
    permission_classes = [IsUser]
    
    def get_queryset(self):
        return Task.objects.all()
    
    def get(self, request):
        user = request.user
        tasks = Task.objects.filter(assigned_to=user.id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TaskUpdateAPIView(APIView):
    
    permission_classes = [IsUser]
    
    def get_queryset(self):
        return Task.objects.all()
    
    def put(self, request, id=None):  
        user = request.user
        
        if id is not None:
            task_id = id
        else:
            task_id = request.data.get('id')
            
        task = Task.objects.get(id=task_id)
        task_status = request.data['status']
        print(task_status)
        data_to_update = request.data.copy()

        if task_status == 'Completed':
            task.assigned_to = user
            task.status = task_status
            task.save()
            # print('saved')
        else:
            task.assigned_to = user
            task.status = task_status
            task.worked_hours = None
            task.completion_report = None
            task.save()
            # print('saved - 2')
            data_to_update['worked_hours'] = None
            data_to_update['completion_report'] = None
            
        serializer = TaskSerializer(task, data=data_to_update, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskReportView(APIView):
    permission_classes = [IsAdminOrSuperAdmin]
    
    def get_queryset(self):
        return Task.objects.all()
    
    def get(self, request, id):
        print(request.user.role)
        try:
            task = Task.objects.get(id=id)
            if task.status == 'Completed':
                report_data = {
                    'id': task.id,
                    'completion_report': task.completion_report,
                    'worked_hours': task.worked_hours,
                    'status': task.status
                }
            else:
                report_data = {
                    'id': task.id,
                    'status': task.status,
                    'message': 'Task is not completed'
                }
            
            return Response(report_data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)