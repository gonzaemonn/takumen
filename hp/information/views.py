from django.shortcuts import render
from .models import Information
from django.views.generic import View


def information(request):
    return render(request, "takumen/top.html")

def informationTest(request):
    if request.method == 'POST':
        mail = request.POST['mail']
        name = request.POST['name']
        kana = request.POST['kana']
        phone = request.POST['phone']
        type = request.POST['type']
        content = request.POST['content']
        order = request.POST['order']
        image = request.POST['image']
        # 検索処理
        return render(request, 'takumen/search.html', {'items': items})
    else:
        return render(request, 'takumen/search.html')