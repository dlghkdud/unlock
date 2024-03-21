from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Follow
from .models import Write

import os
from django.conf import settings

def index(request):
    return render(request, 'unlockk/start.html')

def signup(request):
    return render(request, 'common/signup.html')

def signin(request):
    return render(request, 'common/signin.html')

def picrew(request):
    return render(request, 'unlockk/picrew.html')

def home(request):
    return render(request, 'unlockk/home.html')

def follow(request):
    return render(request, 'unlockk/follow.html')


#팔로우 목록
@login_required(login_url="common:login")
def follow_list(request,user_id):
    follow = get_object_or_404(Follow,user_id=user_id)
    userList = User.objects.exclude(pk=request.user.pk)     #자기자신을 재외하고 불러옴
    
    context = {"follow" : follow , "userList" : userList}
    
    return render(request,"common/follow_list.html",context)


#팔로우
@login_required(login_url="common:login")
def following(request,to_user_id):
    to_user = get_object_or_404(User,pk = to_user_id)
    followUser = get_object_or_404(Follow,user = request.user)
    
    followUser.to_user.add(to_user)

    return redirect('common:follow_list',user_id = request.user.id)


#언팔로우
@login_required(login_url="common:login")
def unfollowing(request,to_user_id):
    to_user = get_object_or_404(User,pk = to_user_id)
    followUser = get_object_or_404(Follow,user = request.user)
    
    followUser.to_user.remove(to_user)
    
    return redirect('common:follow_list',user_id = request.user.id)