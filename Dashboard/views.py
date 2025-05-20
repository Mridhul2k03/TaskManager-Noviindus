from django.shortcuts import render, redirect
from django.views.generic import TemplateView,DeleteView,DetailView,UpdateView,CreateView
from API.models import User, Task
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import AssignTaskForm,UserForm,LoginForm,UserRollForm
from django.urls import reverse_lazy
from API.permissions import IsAdminUser, IsSuperAdminUser, IsAdminOrSuperAdmin, IsUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

# Create your views here.

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.role == 'superadmin' or user.role == 'admin':
            context['tasks'] = Task.objects.all()
        else:
            context['tasks'] = Task.objects.filter(assigned_to=user.id)
        return context

class TaskEditView(LoginRequiredMixin,UpdateView):
    template_name = 'task_edit.html'
    model = Task
    form_class = AssignTaskForm
    success_url = reverse_lazy('index')
    login_url = 'login'


class CreateTaskView(LoginRequiredMixin,CreateView):
    template_name = 'task_edit.html'
    model = Task
    form_class = AssignTaskForm
    success_url = reverse_lazy('index')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in ['admin', 'superadmin']:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return super().dispatch(request, *args, **kwargs)
    
    
class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in ['superadmin']:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return super().dispatch(request, *args, **kwargs)
    
    


# users 

class UsersView(TemplateView):
    template_name = 'users.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class UserEditView(LoginRequiredMixin,UpdateView):
    template_name = 'user_edit.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in ['superadmin']:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return super().dispatch(request, *args, **kwargs)


class CreateUserView(LoginRequiredMixin,CreateView):
    template_name = 'user_edit.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in ['superadmin']:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return super().dispatch(request, *args, **kwargs)


class UserAddRoleView(LoginRequiredMixin,CreateView):
    template_name = 'user_edit.html'
    model = User
    form_class = UserRollForm
    success_url = reverse_lazy('users')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in ['superadmin']:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return super().dispatch(request, *args, **kwargs)
    
    
class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users')
    pk_url_kwarg = 'pk'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in ['superadmin']:
            return HttpResponseForbidden("You are not authorized to access this page.")
        return super().dispatch(request, *args, **kwargs)


class CompletedTask(TemplateView):
    template_name = 'completed_task.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.role == 'superadmin' or user.role == 'admin':
            context['tasks'] = Task.objects.filter(status = 'Completed')
        return context