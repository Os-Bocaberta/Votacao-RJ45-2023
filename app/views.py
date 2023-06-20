from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def vote(request):
    return render(request, 'vote.html')


def result(request):
    return render(request, 'result.html')
