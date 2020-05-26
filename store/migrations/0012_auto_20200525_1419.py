# Generated by Django 3.0.4 on 2020-05-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='average_rating',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AddField(
            model_name='book',
            name='review_count',
            field=models.CharField(default=0, max_length=64),
        ),
    ]
