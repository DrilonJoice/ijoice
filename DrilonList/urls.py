from django.conf.urls import url, include
from django.contrib import admin
from JAList import views 







urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.applicant, name='applicant'),                        
    url(r'^new_stuin$', views.new_stuin, name='new_stuin'),       
    url(r'^(\d+)/add_applicant$', views.add_applicant, name='add_applicant'),      
    url(r'^(\d+)/view_stuin$', views.view_stuin, name='view_stuin'),  
    
    url(r'^edit/(?P<id>\d+)$', views.edit,name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update,name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete,name='delete'),
    
    url(r'^sschool_record$', views.sschool_record, name='sschool_record'),
    url(r'^sscholarship$', views.sscholarship, name='sscholarship'),
    url(r'^sstatus$', views.sstatus, name='sstatus'),

     



    ]


'''
urlpatterns = [    
    url('admin/',admin.site.urls),
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^new$', views.new_list, name='new_list'),   
    url(r'^(\d+)/$', views.view_list, name='view_list'),    
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),

    url(r'^aapplicant$', views.aapplicant, name='aapplicant'),
    url(r'^sstudentinfo$', views.sstudentinfo, name='sstudentinfo'),
    

    url(r'^sschool_record$', views.sschool_record, name='sschool_record'),
    url(r'^sscholarship$', views.sscholarship, name='sscholarship'),
    url(r'^sstatus$', views.sstatus, name='sstatus'),


  ]
 ''' 
