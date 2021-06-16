from django.conf.urls import url, include
from django.contrib import admin
from JAList import views 

urlpatterns = [    
    url('admin/',admin.site.urls),
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^JAList/new$', views.new_list, name='new_list'),   
    url(r'^JAList/(\d+)/$', views.view_list, name='view_list'),    
    url(r'^JAList/(\d+)/add_item$', views.add_item, name='add_item'),

    url(r'^aapplicant$', views.aapplicant, name='aapplicant'),
   	url(r'^sstudentinfo$', views.sstudentinfo, name='sstudentinfo'),
   	

   	url(r'^sschool_record$', views.sschool_record, name='sschool_record'),
   	url(r'^sscholarship$', views.sscholarship, name='sscholarship'),
   	url(r'^sstatus$', views.sstatus, name='sstatus'),


  ]
