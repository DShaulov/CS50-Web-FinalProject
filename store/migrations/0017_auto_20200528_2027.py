# Generated by Django 3.0.4 on 2020-05-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20200528_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=3600),
        ),
    ]