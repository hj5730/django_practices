from django.http import HttpResponse
from django.shortcuts import render


def hello1(request):
    return HttpResponse('<h1>Hello world</h1>', content_type='text/html; charset=utf-8')