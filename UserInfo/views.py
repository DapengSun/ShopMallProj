#coding:utf-8
from django.shortcuts import render

# Create your views here.

# 获取用户信息
def getUserInfo(request):
    return render(request,'userInfo.html')