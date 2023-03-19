from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField('タイトル', max_length=128)
    price = models.CharField('値段', max_length=128)
    description = models.TextField('説明', blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title