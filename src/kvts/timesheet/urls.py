""" URLs for timesheets """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:person_id>/', views.person_view, name='person'),
    path('person/<int:person_id>/<int:day_id>/', views.personday_view, name='personday'),
]
