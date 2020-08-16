""" URLS for timesheets """
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:person_id>/', views.person_view, name='person'),
    path('person/<int:person_id>/<int:day_id>/', views.personday_view, name='personday'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
