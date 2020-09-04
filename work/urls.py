from django.urls import path
from work import views

urlpatterns = [
  path('', views.index, name='index'),
  path('menu', views.menu, name='menu'),
  path('special', views.special, name='special'),
  path('about', views.about, name='about'),
  path('contact', views.contact, name='contact'),
  path('quickList', views.quickList, name='quickList')
]