# Generated by Django 3.0.4 on 2020-05-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='top_seller',
            field=models.BooleanField(default=False),
        ),
    ]
