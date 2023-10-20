from django.urls import path
from . import views as cv

urlpatterns = [
    path('child_1/', cv.show)
]
