from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def mypage(request):
    return render(request, 'mypage.html')