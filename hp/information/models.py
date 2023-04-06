from django.db import models
from django.conf import settings
from django import forms

# Create your models here.
class Information(models.Model):
    mail = models.CharField('メールアドレス', max_length=128)
    name = models.CharField('名前', max_length=128)
    kana = models.CharField('ふりがな', max_length=128)
    phone = models.CharField('電話番号', max_length=128)
    content = models.TextField('お問合せの内容', blank=True)
    content2 = models.TextField('お問合せの内容', blank=True)
    order = models.TextField('ご注文番号', blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('mail','name','kana','phone','content','content2','order','image')