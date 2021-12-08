from django.urls import path

from . import views

app_name = 'megasena'

urlpatterns = [
    path('', views.home, name='home'),
]