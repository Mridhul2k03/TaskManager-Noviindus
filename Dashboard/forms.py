from django import forms
from API.models import User, Task

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AssignTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
                    'title': forms.TextInput(attrs={
                        'class': 'form-control my-2',
                        'placeholder': 'Task Title'
                    }),
                    'description': forms.Textarea(attrs={
                        'class': 'form-control my-2',
                        'placeholder': 'Task Description'
                    }),
                    'assigned_to': forms.Select(attrs={
                        'class': 'form-control my-2',
                        'placeholder': 'Select User'
                    }),
                    'due_date': forms.DateInput(attrs={
                        'type': 'date',
                        'class': 'form-control my-2 w-50',
                        'placeholder': 'YYYY-MM-DD'
                    }),
                    'status': forms.Select(attrs={
                        'class': 'form-control my-2 w-50',
                        'placeholder': 'Select Status'
                    }),
                    'completion_report': forms.Textarea(attrs={
                        'class': 'form-control my-2',
                        'placeholder': 'Completion Report'
                    }),
                    'worked_hours': forms.NumberInput(attrs={
                        'class': 'form-control my-2 w-25',
                        'placeholder': 'Hours Worked'
                    }),     
                }

        labels = {
            'assigned_to': 'Assign To',
            'title': 'Title',
            'description': 'Description',
            'due_date': 'Due Date',
            'status': 'Status',
            'completion_report': 'Completion Report',
            'worked_hours': 'Worked Hours'
            
            
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role','email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Password'
            }),
            'role': forms.Select(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Select Role'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Email'
            }),
        }

        labels = {
            'username': 'Username',
            'password': 'Password',
            'role': 'Role',
            'email': 'Email'
        }

class UserRollForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['role']
    
        widgets = {
            'role': forms.Select(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Select Role'
            }),
        }

        labels = {
            'role': 'Role',
        }