from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, 'helloworld/main.html')

def hello1(request):
    name = request.GET["name"]
    return HttpResponse(f'<h1>Hello {name}</h1>', content_type='text/html; charset=utf-8')

def tags(request):
    return render(request, 'helloworld/tags.html')

def form(request):
    return render(request, 'helloworld/form.html')

def join(request):
    email = request.POST['email']
    password = request.POST['password']
    # 이렇게 하면 터미널 창에 데이터 받은 정보가 뜸.
    # (html 창에서 이메일 비밀번호 친 값이 터미널에 뜸)
    # get으로 하면 데이터가 다 떠서 보안에 취약함. URL에 아이디랑 비밀번호가 다 뜨니까
    # 따라서 POST로 바꿔서 데이터를 보호함. (URL에 안뜨게 함)
    gender = request.POST["gender"]
    hobbies = request.POST.getlist("hobbies")
    # 터미널 창에 체크표시한 것을 리스트로 받기 위하여 .getlist 사용
    description = request.POST["desc"]

    print(email, password, gender, hobbies, description)
    return HttpResponse('ok', content_type='text/plain; charset=utf-8')