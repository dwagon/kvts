""" Admin interface """
from django.contrib import admin
from .models import Day, Fortnight

admin.site.register(Fortnight)
admin.site.register(Day)

# EOF
