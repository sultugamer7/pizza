from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Pizzas
class Pizza(models.Model):
    name = models.CharField(max_length=255)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    # String representation of self
    def __str__(self):
        return f"{self.name} ||| Price: Small / Large: ${self.small_price} / ${self.large_price}"


# Toppings
class Topping(models.Model):
    name = models.CharField(max_length=64)
    # String representation of self
    def __str__(self):
        return f"{self.name}"


# Subs
class Sub(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    # String representation of self
    def __str__(self):
        return f"{self.name} ||| Price: Small / Large: ${self.small_price} / ${self.large_price}"


# Pasta
class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # String representation of self
    def __str__(self):
        return f"{self.name} Pasta ||| Price: ${self.price}"


# Salads
class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # String representation of self
    def __str__(self):
        return f"{self.name} (Salad) ||| Price: ${self.price}"


# Dinner Platters
class Dinner_Platter(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    # String representation of self
    def __str__(self):
        return f"{self.name} (Dinner Platter) ||| Price: Small / Large: ${self.small_price} / ${self.large_price}"


# Order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    status = models.CharField(max_length=64, default="Initiated")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    # String representation of self
    def __str__(self):
        return f"{self.pk} - {self.user} ||| Status: {self.status} ||| Total: ${self.order_total} ||| Date: {self.date}"


# Shopping Cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    cart_item = models.CharField(max_length=64)
    extras = models.CharField(max_length=512)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)
    # String representation of self
    def __str__(self):
        return f"{self.pk} - {self.user}  |  Order ID: {self.order_id}  |  Item: {self.cart_item}  |  Extras: {self.extras}  |  Price: {self.item_price}"


# Extras for subs
class Extra(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # String representation of self
    def __str__(self):
        return f"{self.name} ||| Price: ${self.price}"
