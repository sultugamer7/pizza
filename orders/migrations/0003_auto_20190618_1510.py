# Generated by Django 2.0.3 on 2019-06-18 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("orders", "0002_auto_20190618_1428")]

    operations = [
        migrations.RenameModel(old_name="Dinner_Platters", new_name="Dinner_Platter"),
        migrations.RenameModel(old_name="Salads", new_name="Salad"),
        migrations.RenameModel(old_name="Subs", new_name="Sub"),
        migrations.RenameModel(old_name="Toppings", new_name="Topping"),
    ]
