""" Admin interface """
from django.contrib import admin
from .models import Person, Day, Interval

# Register your models here.
admin.site.register(Person)
admin.site.register(Day)
admin.site.register(Interval)
