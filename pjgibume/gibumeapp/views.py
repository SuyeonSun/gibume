from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def mypage(request):
    return render(request, 'mypage.html')

def detail(request):
    return render(request, 'detail.html')

def product(request):
    return render(request, 'product.html')

def community(request):
    return render(request,'community.html')