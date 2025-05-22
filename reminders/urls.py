from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/reminders/', views.api_reminders, name='api_reminders'),
]
