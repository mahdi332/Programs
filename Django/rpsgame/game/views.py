import random as rn
from django.shortcuts import render , get_object_or_404 
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from .models import GameARR
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate , login , logout
from django.contrib.auth.decorators import login_required 
# Create your views here.
def menu(request):
    return render(request,'game/menu.html')

@login_required(login_url='/accounts/login_section')
def gameview(request):
    GA=GameARR.objects.all()
    return render(request , 'game/gameview.html' , {"GA":GA} )
def results(request):
    choice=(GameARR.objects.get(pk=request.POST['choice'])).choice_text
    computer=(GameARR.objects.get(pk=rn.randint(1,3))).choice_text
    def gamefunc(arg1,arg2):
        if arg1 == arg2:
            return 2
        elif arg1=='ROCK' and arg2=='SCISSORS':
            return 1
        elif arg1=='ROCK' and arg2=='PAPER':
            return 0    
        elif arg1=='SCISSORS' and arg2=='PAPER':
            return 1
        else :
            return not(gamefunc(arg2,arg1))
    result_game=gamefunc(choice,computer)
    if result_game==1:
        current_user=request.user.history
        current_user.historyarr = current_user.historyarr + "1"
        current_user.save()
        print(current_user.historyarr)
        result_game="You Won"
    elif result_game==0:
        current_user=request.user.history
        current_user.historyarr= current_user.historyarr + "0"
        current_user.save()

        print(current_user.historyarr)
        result_game="You Lose"
    else:
        current_user=request.user.history
        current_user.historyarr= current_user.historyarr + "2"
        current_user.save()
        print(current_user.historyarr)
        result_game="You Tie"

    return render (request , 'game/results.html',{"res_game":result_game})