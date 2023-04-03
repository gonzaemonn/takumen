from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
    title = models.CharField('タイトル', max_length=128)
    slug = models.SlugField()
    price = models.IntegerField()
    description = models.TextField('説明', blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_item_price(self):
        return self.quantity * int(self.item.price)# int()でキャストしないとerrorが出る。モデルが悪い？

    def __str__(self):
        return f'{self.item.title}:{self.quantity}'

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
    
    def __str__(self):
        return self.user.email