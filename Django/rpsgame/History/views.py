from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def history(request):
    sum=0
    counter=0
    arr=[]
    current_user=request.user.history
    if current_user.historyarr:
        for i in current_user.historyarr:
            if i=="1":
                sum+=100
            elif i=="0":
                sum+=0
            counter+=1
            arr.append(i)
        avg=sum/counter
        current_user.winrate=avg
        return HttpResponse(f"{current_user.winrate}<br> {arr} ")
    else:
        return HttpResponse("There is no history")