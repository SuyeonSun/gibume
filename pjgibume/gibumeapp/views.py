from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfume
from .models import Comment
from .models import User
from django.utils import timezone
from django.db.models import Q
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')

def mypage(request):
    return render(request, 'mypage.html')

def detail(request):
    return render(request, 'detail.html')

def test(request):
    return render(request, 'test.html')

def product(request, name):
    product = Perfume.objects.get(pk=name)
    #comments=Comment.objects.filter(name=name)
    comments=Comment.objects.filter(name=name).order_by('-yes_count') #
    comment_list=list(comments)
    return render(request, 'product.html', {'product' : product, 'comment_list' : comment_list})

@login_required
# 댓글 작성
def writecomment(request, name):
    comment=Comment()
    comment.name = Perfume.objects.get(pk=name)
    comment.content=request.POST.get('content',False)
    comment.pub_date=timezone.datetime.now()
    comment.author=request.user
    comment.save()
    return redirect("product", name)

# 댓글 삭제
@login_required
def deletecomment(request, name, id):
    comment = get_object_or_404(Comment, pk=id)
    if comment.author != request.user.nickname:
        return redirect("product", name)
    else:
        comment.delete()
        return redirect("product", name)

def community(request):
    return render(request,'community.html')

def community_detail(request):
    return render(request, 'community_page.html')


def perfume(request):

    perfume_list = Perfume.objects.all()

    return render(request, 'perfume.html', {'perfume_list' : perfume_list})

def search(request):
    search_list = Perfume.objects.all()

    search_key = request.POST.get('search_key')
    if search_key:
        search_list = search_list.filter(Q(name__icontains=search_key) | Q(brand__icontains=search_key))

    return render(request, 'search.html', {'search_list' : search_list, 'search_key':search_key})


def education(request):
    return render(request, 'education.html')

#like
# @login_required
def like_post(request, name):
    product = Perfume.objects.get(pk=name)
    if request.user.is_authenticated: #
        if request.user in product.like_users.all():
            product.like_users.remove(request.user)
            # product.like_count -= 1
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

    if not request.user.is_authenticated: #
        return redirect("login") # 

#ok
# @login_required
def ok_post(request, name):
    product = Perfume.objects.get(pk=name)
    if request.user.is_authenticated: #
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
    
    if not request.user.is_authenticated: #
        return redirect("login") # 

#dislike
# @login_required
def dislike_post(request, name):
    product = Perfume.objects.get(pk=name)
    if request.user.is_authenticated: #
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

    if not request.user.is_authenticated: #
        return redirect("login") # 

# 댓글 좋아요
# @login_required
def yesUp(request,name,id):
    yes = get_object_or_404(Comment, id=id)
    if request.user.is_authenticated: #
        if request.user in yes.yes_users.all():
            yes.yes_users.remove(request.user)
            yes.yes_count-=1 ###
            yes.save() ###
        else:
            if request.user in yes.no_users.all():
                yes.no_users.remove(request.user)
                yes.no_count-=1 ###
                yes.yes_users.add(request.user)
                yes.yes_count+=1 ###
                yes.save() ###
            else:
                yes.yes_users.add(request.user)
                yes.yes_count+=1 ###
                yes.save() ###
        return redirect("product", name)

    if not request.user.is_authenticated: #
        return redirect("login") # 

# 댓글 싫어요
# @login_required
def noUp(request,name,id):
    no = get_object_or_404(Comment, id=id)
    if request.user.is_authenticated: #
        if request.user in no.no_users.all(): 
            no.no_users.remove(request.user)
            no.no_count-=1 ###
            no.save() ###
        else:
            if request.user in no.yes_users.all():
                no.yes_users.remove(request.user)
                no.yes_count-=1 ###
                no.no_users.add(request.user)
                no.no_count+=1 ###
                no.save() ###
            else:
                no.no_users.add(request.user)
                no.no_count+=1 ###
                no.save() ###
        return redirect("product", name)

    if not request.user.is_authenticated: #
        return redirect("login") # 