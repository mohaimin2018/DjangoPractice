from django.shortcuts import render

# Create your views here.

def details(request):

    name = 'Mohai'
    age = 27
    gender = 'Male'

    mydict = {'name':name, 'age':age, 'gender':gender}

    return render(request,'info/index.html',context=mydict)