from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Parfum(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500, blank=True)
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=59.99)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'perfumes'

    def get_absolute_url(self):
        return reverse('perfum-info', args=[self.slug])

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    amount_paid = models.FloatField(null=True)
    shipping_address = models.TextField(max_length=1000, null=True)
    phone = models.CharField(max_length=20, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Order - #' + str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    perfum = models.ForeignKey(Parfum, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return 'Order Item - #' + str(self.id)



