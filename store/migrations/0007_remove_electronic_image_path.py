# Generated by Django 3.0.4 on 2020-05-07 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200507_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electronic',
            name='image_path',
        ),
    ]
