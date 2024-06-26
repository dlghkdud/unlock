from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'unlockk'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', auth_views.LoginView.as_view(template_name='unlockk/signin.html'), name='signin'),
    path('signup/', views.signup, name='signup'),
    path('picrew/', views.picrew, name='picrew'),
    path('home/', views.home, name='home'),
    path('write/<int:object_id>/', views.write_page, name='write'),
    path('friend-request/<int:friend_request_id>/accept/', views.friend_accept, name='friend-accept'),
    path('friend-request/<int:friend_request_id>/reject/', views.friend_reject, name='friend-reject'),
    path('friend_remove/<int:friend_id>/', views.friend_remove, name='friend_remove'),
    path('friend_list/', views.friend_list, name='friend_list'),
]
