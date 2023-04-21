from django.urls import path
from . import views

app_name = 'server.apps.portfolio'

urlpatterns = [
    path('', views.index, name='index'),
]