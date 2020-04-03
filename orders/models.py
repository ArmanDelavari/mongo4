from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# ta alan sabade kharid nud alan sefareshe kala
from shop.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)   # mikhaym bebinim pardakht shode ya na

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.user} {str(self.id)}"

    def get_total_price(self):
        return sum(item.get_cost() for item in self.item.all())


class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()  # be khatere zarin bap hatman bayad integer bashe
    tedad = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.tedad


# coopone kode takhfif
class Copon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    valid_from = models.DateTimeField()  # az key etebar dashte bashe
    valid_to = models.DateTimeField()   # ta key
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])   # cheghad mikhaym takhfif bedim, va min va max baraye adado injoori midim
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code