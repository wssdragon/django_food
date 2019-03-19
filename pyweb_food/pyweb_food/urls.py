"""pyweb_food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boardList/', views.boardList)
]

# 디버그 툴바 관련 url mapping
if settings.DEBUG: # settings.py 의 DEBUG 변수 가져옴
	import debug_toolbar # debug_toolbar 기능을 가져옴
	#debug_toolbar 의 url 패턴 정의
	urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]