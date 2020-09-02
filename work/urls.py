from django.urls import path
from work import views

urlpatterns = [
  path('', views.index, name='index'),
]