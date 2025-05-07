from django.contrib import admin
from.models import Task, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Task)
class MainUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )

admin.site.register(User, MainUserAdmin)