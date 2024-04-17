from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
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

def write(request):
    return render(request, 'unlockk/write.html')

def follow(request):
    kw = request.GET.get('kw', '')  # 검색어
    user_list = []  # 검색 결과를 담을 리스트 초기화

    if kw:
        # 검색어를 포함한 사용자를 필터링하여 리스트에 추가
        user_list = User.objects.filter(Q(username__icontains=kw))

    context = {'kw': kw, 'user_list': user_list}
    return render(request, 'unlockk/follow.html', context)


# 팔로우 목록
@login_required(login_url='common:signin')
def follow_list(request, user_id):
    follow = get_object_or_404(Follow, user_id = user_id)
    users = User.objects.exclude(pk = request.user.pk)     # 자기자신을 제외하고 불러옴
    
    context = {'follow': follow , 'users': users}
    return render(request, 'unlockk/follow.html', context)
    
    
# 팔로우
@login_required(login_url='common:signin')
def following(request, to_user_id):
    to_user = get_object_or_404(User, pk = to_user_id)
    followUser = get_object_or_404(Follow, user = request.user)
    
    followUser.to_user.add(to_user)

    return redirect('unlockk:follow_list', user_id = request.user.id)
    
# 언팔로우
@login_required(login_url='common:signin')
def unFollowing(request, to_user_id):
    to_user = get_object_or_404(User, pk = to_user_id)
    followUser = get_object_or_404(Follow, user = request.user)
    
    followUser.to_user.remove(to_user)
    
    return redirect('unlockk:follow_list', user_id = request.user.id)