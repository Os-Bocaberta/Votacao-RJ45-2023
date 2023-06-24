from django.shortcuts import render, redirect
from .models import Candidates, Voters
from django.contrib.sessions.backends.db import SessionStore
import csv

# Create your views here.


def home(request):
    return render(request, 'home.html')


def vote(request):
    try:
        candidates = Candidates.objects.values()
        candidates_king = []
        candidates_queen = []
        registration = request.GET.get('matricula')
        result = Voters.objects.filter(registration=registration, status=False)

        if result:
            request.session['registration'] = registration

            for c in candidates:
                if c['type'] in 'kK':
                    candidates_king.append(c)
                elif c['type'] in 'qQ':
                    candidates_queen.append(c)
                else:
                    pass

            return render(request, 'vote.html', {'c_king': candidates_king, 'c_queen': candidates_queen})
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
    try:
        datas_result_king = {}
        datas_result_queen = {}
        total_vote_king = 0
        total_vote_queen = 0

        candidates_king = Candidates.objects.filter(type='k')
        candidates_queen = Candidates.objects.filter(type='q')
        votes_king = Voters.objects.values('vote_king')
        votes_queen = Voters.objects.values('vote_queen')

        for index in candidates_king:
            i = str(index.id)
            datas_result_king[i] = [0, index.name]

        for index in candidates_queen:
            i = str(index.id)
            datas_result_queen[i] = [0, index.name]

        for index in votes_king:
            if index['vote_king']:
                index_king = str(index['vote_king'])
                if index_king in datas_result_king:
                    datas_result_king[index_king][0] += 1

        for index in votes_queen:
            if index['vote_queen']:
                index_queen = str(index['vote_queen'])
                if index_queen in datas_result_queen:
                    datas_result_queen[index_queen][0] += 1

        for i in datas_result_king.values():
            total_vote_king += i[0]

        for i in datas_result_queen.values():
            total_vote_queen += i[0]

        for i in datas_result_king.values():
            i[0] = str((i[0] / total_vote_king) * 100).replace(',', '.')

        for i in datas_result_queen.values():
            i[0] = str((i[0] / total_vote_queen) * 100).replace(',', '.')

        result_king_sorted = dict(
            sorted(datas_result_king.items(), key=lambda x: x[1][0], reverse=True))
        result_queen_sorted = dict(
            sorted(datas_result_queen.items(), key=lambda x: x[1][0], reverse=True))

        king_three = list(result_king_sorted.items())[:3]
        rendering_king = {}
        queen_three = list(result_queen_sorted.items())[:3]
        rendering_queen = {}

        for i, (chave, valor) in enumerate(king_three):
            rendering_king[str(i)] = valor

        for i, (chave, valor) in enumerate(queen_three):
            rendering_queen[str(i)] = valor

        return render(request, 'result.html', {'king': rendering_king, 'queen': rendering_queen})
    except:
        return redirect('home')
