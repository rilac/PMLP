from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    if request.method == 'POST':
        userid = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, id=userid, password=password)

        if user is not None:
            print("메인 화면으로 뷰 옮기기")
        else:
            print("인증 실패 출력")