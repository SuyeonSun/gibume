from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfume
from .models import Comment
from .models import User
from django.utils import timezone
from django.contrib import auth

from django.contrib.auth.decorators import login_required

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
    perfume_list = Perfume.objects.all()
    return render(request, 'perfume.html', {'perfume_list' : perfume_list})

def education(request):
    return render(request, 'education.html')

# love
# @login_required
# def love_post(request, name):
#     product = Perfume.objects.get(pk=name)
#     if request.user in product.love_users.all():
#         product.love_users.remove(request.user)
#         product.love_count -= 1
#         product.save()
#     else:
#         product.love_users.add(request.user)
#         product.love_count += 1
#         product.save()
#     return redirect("product", name)

#like
@login_required
def like_post(request, name):
    product = Perfume.objects.get(pk=name)
    if request.user in product.like_users.all():
        product.like_users.remove(request.user)
        #product.like_count -= 1
        product.save()
    else:
        if request.user in product.ok_users.all():
            product.ok_users.remove(request.user)
            #product.ok_count -= 1
            product.like_users.add(request.user)
            #product.like_count += 1
            product.save()

        if request.user in product.dislike_users.all():
            product.dislike_users.remove(request.user)
            #product.dislike_count -= 1
            product.like_users.add(request.user)
            #product.like_count += 1
            product.save()
        else:
            product.like_users.add(request.user)
            #product.like_count += 1
            product.save()
    return redirect("product", name)

#ok
@login_required
def ok_post(request, name):
    product = Perfume.objects.get(pk=name)
    if request.user in product.ok_users.all():
        product.ok_users.remove(request.user)
        # product.ok_count -= 1
        product.save()
    else:
        if request.user in product.like_users.all():
            product.like_users.remove(request.user)
            #product.like_count -= 1
            product.ok_users.add(request.user)
            #product.ok_count += 1
            product.save()

        if request.user in product.dislike_users.all():
            product.dislike_users.remove(request.user)
            #product.dislike_count -= 1
            product.ok_users.add(request.user)
            #product.ok_count += 1
            product.save()

        else:
            product.ok_users.add(request.user)
            #product.ok_count += 1
            product.save()
    return redirect("product", name)

#dislike
@login_required
def dislike_post(request, name):
    product = Perfume.objects.get(pk=name)
    if request.user in product.dislike_users.all():
        product.dislike_users.remove(request.user)
        #product.dislike_count -= 1
        product.save()
    else:
        if request.user in product.like_users.all():
            product.like_users.remove(request.user)
            #product.like_count -= 1
            product.dislike_users.add(request.user)
            #product.dislike_count += 1
            product.save()

        if request.user in product.ok_users.all():
            product.ok_users.remove(request.user)
            #product.ok_count -= 1
            product.dislike_users.add(request.user)
            #product.dislike_count += 1
            product.save()

        else:
            product.dislike_users.add(request.user)
            #product.dislike_count += 1
            product.save()
    return redirect("product", name)
