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

def community_detail(request):
    return render(request, 'community_page.html')

def perfume(request):
    return render(request, 'perfume.html')

def education(request):
    return render(request, 'education.html')

def test(request):
    return render(request, 'test.html')

def form(request):
    return render(request, 'form.html')

def result(request):
    return render(request, 'result.html')