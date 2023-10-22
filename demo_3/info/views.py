from django.shortcuts import render

# Create your views here.

def details(request):

    name = 'Mohai Minul Islam'
    age = 27
    gender = 'Male'

    mydict = {'name':name, 'age':age, 'gender':gender,'address':''}

    return render(request,'info/index.html',context=mydict)