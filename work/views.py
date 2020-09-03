from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

depts_list = [
  {'no': 10, 'name': '财务部', 'location': '北京'},
  {'no': 20, 'name': '研发部', 'location': '成都'},
  {'no': 30, 'name': '销售部', 'location': '上海'}
]

def index(request):
  return render(request, 'index.html', {'depts_list': depts_list})

def menu(request):
  return render(request, 'menu.html', {'depts_list': depts_list})

def special(request):
  return render(request, 'special.html', {'depts_list': depts_list})

def about(request):
  return render(request, 'about.html', {'depts_list': depts_list})

def contact(request):
  return render(request, 'contact.html', {'depts_list': depts_list})
