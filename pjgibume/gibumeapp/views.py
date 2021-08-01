from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfume
from .models import Comment
from django.utils import timezone
from django.db.models import Q

# Create your views here.


def home(request):
    return render(request, 'home.html')

def mypage(request):
    return render(request, 'mypage.html')

def detail(request):
    return render(request, 'detail.html')

def product(request, name):
    product = Perfume.objects.get(pk=name)
    comments=Comment.objects.filter(name=name)
    comment_list=list(comments)
    return render(request, 'product.html', {'product' : product, 'comment_list' : comment_list})

# 댓글 작성
def writecomment(request, name):
    comment=Comment()
    comment.name = Perfume.objects.get(pk=name)
    comment.content=request.POST.get('content',False)
    comment.pub_date=timezone.datetime.now()
    comment.save()
    return redirect("product", name)

def community(request):
    return render(request,'community.html')

def community_detail(request):
    return render(request, 'community_page.html')


def perfume(request):
    perfume_list = Perfume.objects.all() # 분류

    return render(request, 'perfume.html', {'perfume_list' : perfume_list})

def search(request):
    search_list = Perfume.objects.all()

    search_key = request.POST.get('search_key')
    if search_key:
        search_list = search_list.filter(Q(name__icontains=search_key) | Q(brand__icontains=search_key))

    return render(request, 'search.html', {'search_list' : search_list, 'search_key':search_key})

def education(request):
    return render(request, 'education.html')



