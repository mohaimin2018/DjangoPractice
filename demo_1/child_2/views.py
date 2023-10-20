from django.shortcuts import render

# Create your views here.

def show(request):

    return render(request,'child_2/index.html')
