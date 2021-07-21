"""pjgibume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from gibumeapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('mypage', mypage, name = "mypage"),
    path('detail/',detail,name="detail"),

    # product 페이지 
    path('product/<str:name>',product,name="product"),
    path('product/<str:name>/writecomment/', writecomment, name="writecomment"),
    
    path('like/<str:id>/', like_post, name="like_post"),

    path('community/', community, name="community"),
    path('community_detail/', community_detail, name="community_detail"),
    path('perfume/', perfume, name = "perfume"),
    path('education/',education,name="education"),
    path('account/', include('account.urls')),

]
