# Generated by Django 2.0.3 on 2019-06-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("orders", "0007_auto_20190621_1201")]

    operations = [
        migrations.AlterField(
            model_name="cart", name="order_id", field=models.IntegerField()
        )
    ]
