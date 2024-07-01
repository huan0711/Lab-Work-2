# plotapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plot_view, name='plot_view'),
]
