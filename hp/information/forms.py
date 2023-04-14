from django import forms

#フォームクラス作成
class Information_Form(forms.Form):
    # Name = forms.CharField(label="名前")                    
    # Tell = forms.IntegerField(label="電話番号")
    # Mail = forms.EmailField(label="メールアドレス")
    # FreeText = forms.CharField(widget=forms.Textarea,label="備考")

    mail = forms.CharField(label='メールアドレス', max_length=128)
    name = forms.CharField(label='名前', max_length=128)
    kana = forms.CharField(label='ふりがな', max_length=128)
    phone = forms.CharField(label='電話番号', max_length=128)
    content = forms.CharField(widget=forms.Textarea,label="備考")
    # image = forms.ImageField(upload_to='images')