from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'unlockk'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', auth_views.LoginView.as_view(template_name='unlockk/signin.html'), name='signin'),
    path('signup/', views.signup, name='signup'),

]
