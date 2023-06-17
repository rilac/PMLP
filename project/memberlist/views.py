from .models import CustomUser
from django.shortcuts import render, redirect
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

def joined(request):
    if request.method == 'POST':
        # 폼에서 전송된 데이터 받기
        username = request.POST['id']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phoneNumber']
        address = request.POST['address']

        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phoneNumber=phone_number,
            address=address
        )

        user.save()

        # 회원 가입 성공 후 리다이렉트 등 필요한 처리
        return redirect('/')
    return render(request, '../templates/sign/signup.html')