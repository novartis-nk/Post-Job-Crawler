from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_the_form_value)
]