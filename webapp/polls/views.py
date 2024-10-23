from django.shortcuts import HttpResponse,render

# Create your views here.

def index(response):
    return HttpResponse("Hello World. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def sample(request):
    return render(request, 'sample.html')

def sample1(request):
    return render(request, 'samplepage1.html')

def sample2(request):
    return render(request, 'samplepage2.html')
