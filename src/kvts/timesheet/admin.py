""" Admin interface """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Day, Fortnight, Employee

admin.site.register(Fortnight)
admin.site.register(Day)
admin.site.register(Employee)


class EmployeeInline(admin.StackedInline):
    """ Admin Interface for Employee """
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    """ Adapt existing user admin """
    inlines = (EmployeeInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# EOF
