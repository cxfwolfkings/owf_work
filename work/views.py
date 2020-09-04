from django.shortcuts import render
from django.http import HttpResponse
from work.models import QuickList
import datetime

# Create your views here.

def index(request):
  return render(request, 'index.html')

def menu(request):
  return render(request, 'menu.html')

def special(request):
  return render(request, 'special.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')

def quickList(request):
  quickList = QuickList.objects.filter(dealTime = datetime.date.today()) 
  return render(request, 'quickList.html', {'quickList': quickList})
