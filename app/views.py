from django.shortcuts import render, redirect
from .models import Candidates, Voters
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.


def home(request):
    return render(request, 'home.html')


def vote(request):
    try:
        registration = request.GET.get('matricula')
        result = Voters.objects.filter(registration=registration, status=False)

        if result:
            request.session['registration'] = registration
            return render(request, 'vote.html')
        else:
            return redirect('home')
    except:
        return redirect('home')


def post_datas(request):
    try:
        if request.method == "POST":
            registration = request.session.get('registration')
            voter = Voters.objects.get(registration=registration, status=False)
            queen = request.POST.get('queen')
            king = request.POST.get('king')

            voter.status = True
            voter.vote_king = f'{king}'
            voter.vote_queen = f'{queen}'
            voter.save()

    except:
        return redirect('home')

    return redirect('result')


def result(request):
    datas_result = {}

    candidates = Candidates.objects.values()
    votes_king = Voters.objects.values('vote_king')

    for index in candidates:
        i = str(index['id'])
        datas_result[i] = 0

    for index in votes_king:
        if index['vote_king']:
            index_king = str(index['vote_king'])
            datas_result[index_king] += 1

    print(datas_result)

    return render(request, 'result.html')
