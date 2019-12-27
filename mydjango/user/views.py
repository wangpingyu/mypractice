from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    return HttpResponse('这是一个demo')

