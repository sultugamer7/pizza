from django.contrib import admin
from .models import (
    Pizza,
    Topping,
    Sub,
    Pasta,
    Salad,
    Dinner_Platter,
    Order,
    Cart,
    Extra,
)

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_Platter)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Extra)
