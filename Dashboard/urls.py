from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('index/',views.IndexView.as_view(),name='index'),
    path('task/<int:pk>/edit/',views.TaskEditView.as_view(),name='task-edit'),
    path('task/create/',views.CreateTaskView.as_view(),name='task-create'),
    path('task/<int:pk>/delete/',views.TaskDeleteView.as_view(),name='task-delete'),
    path('task/completed/',views.CompletedTask.as_view(),name='completed-task'),
    
    path('users/',views.UsersView.as_view(),name='users'),
    path('users/<int:pk>/edit/',views.UserEditView.as_view(),name='user-edit'),
    path('users/create/',views.CreateUserView.as_view(),name='user-create'),
    path('users/<int:pk>/delete/',views.UserDeleteView.as_view(),name='user-delete'),
    path('users/<int:pk>/add-role/',views.UserAddRoleView.as_view(),name='user-add-role'),
    
]