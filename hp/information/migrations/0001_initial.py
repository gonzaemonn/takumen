# Generated by Django 4.2 on 2023-04-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=128, verbose_name='メールアドレス')),
                ('name', models.CharField(max_length=128, verbose_name='名前')),
                ('kana', models.CharField(max_length=128, verbose_name='ふりがな')),
                ('phone', models.CharField(max_length=128, verbose_name='電話番号')),
                ('content', models.TextField(blank=True, verbose_name='お問合せの内容')),
                ('content2', models.TextField(blank=True, verbose_name='お問合せの内容')),
                ('order', models.TextField(blank=True, verbose_name='ご注文番号')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
