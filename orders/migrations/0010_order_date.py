# Generated by Django 2.0.3 on 2019-06-23 06:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("orders", "0009_auto_20190622_1103")]

    operations = [
        migrations.AddField(
            model_name="order",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        )
    ]
