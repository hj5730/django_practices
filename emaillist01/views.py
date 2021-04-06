from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist01 import models

def index(request):
    results = models.findall() # findall(): 모든 문자열을 리스트로 바꿔준다.
    data = {"emaillist_list": results} # 중요한 것은 results가 리스트라는 것. emaillist가 딕셔너리 라는 것.
    return render(request, 'emaillist01/index.html', data) # render : template를 html로 반환

def form(request):
    return render(request, 'emaillist01/form.html')

def add(request):
    firstname = request.POST["fn"]
    lastname = request.POST["ln"]
    email = request.POST["email"]

    models.insert(firstname, lastname, email)

    return HttpResponseRedirect("/emaillist01")