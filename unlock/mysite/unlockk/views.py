from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Friend

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


# 친구신청
@login_required
def friend_request(request, user_id):
    users = User.objects.all()
    if request.method == 'POST':
        from_user = request.user
        to_user = get_object_or_404(User, id=user_id)
        if Friend.objects.filter(from_user=from_user, to_user=to_user).exists():
            messages.error(request, "이미 친구 요청을 보냈습니다.")
        else:
            Friend.objects.create(from_user=from_user, to_user=to_user)
            messages.success(request, "친구 신청을 보냈습니다.")
        return redirect('unlockk:home')
    else:
        return render(request, 'unlockk/follow.html', {'users': users})
 
# 친구신청 수락
@login_required
def friend_accept(request, friend_request_id):
    friend_request = get_object_or_404(Friend, id=friend_request_id)
    if friend_request.to_user != request.user:
        messages.error(request, "권한이 없습니다.")
    elif friend_request.status != 'pending':
        messages.error(request, "이미 처리된 요청입니다.")
    else:
        friend_request.status = 'accepted'
        friend_request.save()
        messages.success(request, "친구 신청을 수락했습니다.")
    return redirect('unlockk:home')

# 친구신청 거절
@login_required
def friend_reject(request, friend_request_id):
    friend_request = get_object_or_404(Friend, id=friend_request_id)
    if friend_request.to_user != request.user:
        messages.error(request, "권한이 없습니다.")
    elif friend_request.status != 'pending':
        messages.error(request, "이미 처리된 요청입니다.")
    else:
        friend_request.status = 'rejected'
        friend_request.save()
        messages.success(request, "친구 신청을 거절했습니다.")
    return redirect('unlockk:home')