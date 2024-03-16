from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'unlockk'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),

]
