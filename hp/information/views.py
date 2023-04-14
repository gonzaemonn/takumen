from django.shortcuts import render
from .models import Information,InformationForm
from django.views.generic import View, TemplateView
from . import forms

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

class FormView(TemplateView):

    # 初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                       "form":forms.Information_Form(),
                       }

    # GET時の処理を記載
    def get(self,request):
        return render(request, "takumen/top.html",context=self.params)

    # POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Information_Form(request.POST)
            
            # フォーム入力が有効な場合
            if self.params["form"].is_valid():
                self.params["Message"] = "入力情報が送信されました。"

        return render(request, "takumen/top.html",context=self.params)