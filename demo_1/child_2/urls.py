from django.urls import path
from . import views as c2v

urlpatterns = [
    path('child_2/', c2v.show)
]
