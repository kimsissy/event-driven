from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, '2index.html')

def page1(request):
    return render(request, '2page1.html')

def page2(request):
    return render(request, '2page2.html')
