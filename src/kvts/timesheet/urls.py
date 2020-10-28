""" URLs for timesheets """
from django.urls import path
from . import views
from . import manage_views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:person_id>/', views.person_view, name='person'),
    path('person/<int:person_id>/<int:day_id>/', views.personday_view, name='personday'),

    path('manage/', manage_views.index, name='manage_index'),
    path('manage/fortnight/', manage_views.fortnight, name='manage_fortnights'),
    path('manage/fortnight/create', manage_views.create_fortnight, name='create_fortnight'),
    path('manage/fortnight/<int:fortnight_id>/edit', manage_views.edit_fortnight, name='edit_fortnight'),
    path('manage/fortnight/<int:fortnight_id>/delete', manage_views.delete_fortnight, name='delete_fortnight'),
    path('manage/fortnight/<int:fortnight_id>/current', manage_views.current_fortnight, name='current_fortnight'),
    path('manage/user/', manage_views.user, name='manage_users'),
]
