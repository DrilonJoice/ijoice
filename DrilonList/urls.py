"""DrilonList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
'''
from django.contrib import admin
from django.urls import path
from JAList.views import JAListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('JAList', JAListView),
]
'''
'''
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
'''
'''
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/',admin.site.urls),

]
'''

'''prev
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^$','lists.view.home_page',name='home'),
'''
'''
from django.conf.urls import url
from django.contrib import admin 
from JAList import views

urlpatterns=[
	url(r'^admin/',admin.site.urls),
	url(r'^$',views.homepage),
]

'''

from django.conf.urls import url
from django.contrib import admin 
from JAList import views

urlpatterns=[
	url(r'^admin/',admin.site.urls),
	url(r'^$',views.mypage),
]