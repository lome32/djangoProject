from django.urls import re_path 

from EmplApp import views 

 

from django.conf.urls.static import static 

from django.conf import settings 

 

urlpatterns=[ 

    re_path(r'^department$',views.departmentApi), 

    re_path(r'^department/([0-9]+)$',views.departmentApi), 

 

    re_path(r'^employees$',views.employeeApi), 

    re_path(r'^employees/([0-9]+)$',views.employeeApi), 

 

    re_path(r'^employees/savefile',views.SaveFile) 

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)