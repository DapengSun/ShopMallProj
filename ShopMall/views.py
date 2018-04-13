# coding:utf-8
from django.shortcuts import render

# Create your views here.

from .models import UserMessage


def getForm(request):
    # all_messages = UserMessage.objects.filter(name='sdp')
    # for i in all_messages:
    #     print i.message

    # if request.method == 'POST':
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message','')
    #     address = request.POST.get('address','')
    #     email = request.POST.get('email','')
    #
    #     userMessage = UserMessage()
    #     userMessage.name = name
    #     userMessage.id = 3
    #     userMessage.email = email
    #     userMessage.address = address
    #     userMessage.message = message
    #     userMessage.save()

    messages = UserMessage.objects.filter(name='sdp')

    return render(request, '留言板.html',{
        "mymessage":messages[0]
    });

