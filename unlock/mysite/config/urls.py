from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from unlockk import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('unlockk/', include('unlockk.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]
