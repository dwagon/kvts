""" Admin interface """
from django.contrib import admin
from .models import Person, Day, Fortnight

admin.site.register(Fortnight)
admin.site.register(Person)
admin.site.register(Day)

# EOF
