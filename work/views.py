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
  # 今天
  today = datetime.date.today()
  if request.GET.get('quickDate') is not None:
    today= datetime.datetime.strptime(request.GET.get('quickDate'),'%Y-%m-%d')
  tomorrow = today + datetime.timedelta(days=1)
  # 查询今天待办事项
  quickList = QuickList.objects.filter(
    dealTime__gte=today, dealTime__lte=tomorrow
  ).order_by('orderNo')
  # 返回视图 
  return render(request, 'quickList.html', {'quickList': quickList})
