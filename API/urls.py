from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('tasks/',views.TaskAPIView.as_view()),
    path('tasks/<int:id>/',views.TaskUpdateAPIView.as_view()),
    path('tasks/<int:id>/report/', views.TaskReportView.as_view(), name='task-report'),
    
]
