from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Parfum(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500, blank=True)
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=59.99)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'perfums'

    def str(self):
        return f'Perfum(title={self.name}, description={self.description}, price={self.price}, slug={self.slug})'

    def repr(self):
        return self.str()

    def get_absolute_url(self):
        return reverse('perfum-info', args=[self.slug])

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    amount_paid = models.FloatField(null=True)
    shipping_address = models.TextField(max_length=1000, null=True)
    phone = models.IntegerField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def register(self):
        self.save

    def str(self):
        return 'Order - #' + str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    perfum = models.ForeignKey(Parfum, on_delete=models.CASCADE, null=True)

    quantity = models.PositiveBigIntegerField(default=1)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def str(self):
        return 'Order Item - #' + str(self.id)


