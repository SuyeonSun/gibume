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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('mypage', mypage, name = "mypage"),
    path('detail1/',detail1,name="detail1"),
    path('detail2/',detail2,name="detail2"),
    path('detail3/',detail3,name="detail3"),
    path('detail4/',detail4,name="detail4"),
    path('detail5/',detail5,name="detail5"),
    path('detail6/',detail6,name="detail6"),
    path('detail7/',detail7,name="detail7"),
    path('detail8/',detail8,name="detail8"),

    # product 페이지 
    path('product/<str:name>',product,name="product"),
    path('product/<str:name>/writecomment/', writecomment, name="writecomment"),
    
    # 선호도
    path('like/<str:name>/', like_post, name="like_post"),
    path('ok/<str:name>/', ok_post, name="ok_post"),
    path('dislike/<str:name>/', dislike_post, name="dislike_post"),
    # 댓글 삭제
    path('product/<str:name>/<str:id>/deletecomment', deletecomment, name="deletecomment"),
    # 댓글 좋아요
    path('product/<str:name>/<str:id>/yesUp', yesUp, name="yesUp"),
    # 댓글 싫어요
    path('product/<str:name>/<str:id>/noUp', noUp, name="noUp"),

    path('community/', community, name="community"),
    path('community/new/', community_new, name="community_new"),
    path('community/create/', create, name="create"),
    path('community_detail/<int:id>', community_detail, name='community_detail'),
    path('community_detail/<int:id>/community_delete', community_delete, name="community_delete"),
    path('community_detail/<int:id>/community_edit', community_edit, name="community_edit"),
    path('community_detail/<int:id>/community_update', community_update, name="community_update"),
    path('community_detail/<int:id>/save_post', save_post, name="save_post"),

    path('community_detail/<int:id>/writecomment/', writeCommunitycomment, name="writeCommunitycomment"), #
    path('community_detail/deletecomment/<int:blog_id>/<int:comment_id>',deleteCommunitycomment,name="deleteCommunitycomment"),

    path('community_detail/<int:blog_id>/<int:comment_id>/Up', Up, name="Up"),
    path('community_detail/<int:blog_id>/<int:comment_id>/Down', Down, name="Down"),

    path('perfume/', perfume, name = "perfume"),
    path('perfume/search', search, name="search"),
    path('education/',education,name="education"),
    path('educommonsense/',common,name="common"),
    path('eduquiz/',eduquiz,name="eduquiz"),
    path('account/', include('account.urls')),

    path('form/', form, name="form"),
    path('test/', result, name="test"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
