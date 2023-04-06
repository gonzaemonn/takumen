from django.shortcuts import render
from .models import Information,InformationForm
from django.views.generic import View

def information(request):
    return render(request, "information/information.html")

def informationTest(request):
    f = InformationForm()
    return render(request, 'information/informationTest.html',{'form':f})

def information_model(request):
    if request.method == "POST":
        # form = InformationForm(request.POST)
        name    = request.POST["name"]
        kana    = request.POST["kana"]
        form       = Information(name=name, kana=kana)
        form.save() 
        return render(request, "takumen/top.html")
        # if form.is_valid():
        #     form.save()
        #     return render(request, "takumen/top.html")   
        # else:
        #     return render(request, "information/information.html")