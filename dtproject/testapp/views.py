from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def datetimeinfo_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='<h1> Hello Friend,'
    if h<12:
        msg=msg+'Good Morning'
    elif h<16:
        msg=msg+'Good Afternoon'
    elif h<21:
        msg=msg+'Good Evening'
    else:
        msg=msg+'Good Night'
    msg=msg+'</h1><hr>'
    msg=msg+'<h1> Now Server Date and Time is :'+str(date)+'</h1>'
    print(msg) #it will print on server console not for enduser
    return HttpResponse(msg)


