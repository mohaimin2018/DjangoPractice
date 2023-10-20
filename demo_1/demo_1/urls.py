
from django.contrib import admin
from django.urls import path,include
from child_1 import urls as c1u
from child_2 import urls as c2u


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(c1u)),
    path('',include(c2u)),
]
