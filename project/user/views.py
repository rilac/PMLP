from django.shortcuts import render
from django.contrib.auth import authenticate


# Create your views here.

def signup(request):
    return render(request, '../templates/sign/signup.html')


def login(request):
    # 이런 식으로 코딩하면 되겠다이지 여기에 맞추는 건 아닙니다.
    if request.method == 'POST':
        userid = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, id=userid, password=password)

        if user is not None:
            print("메인 화면으로 뷰 옮기기")
        else:
            print("인증 실패 출력")

