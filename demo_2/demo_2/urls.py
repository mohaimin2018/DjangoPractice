
from django.contrib import admin
from django.urls import path, include
from student import urls as s_url
from teacher import urls as t_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(s_url)),
    path('',include(t_url)),

]
