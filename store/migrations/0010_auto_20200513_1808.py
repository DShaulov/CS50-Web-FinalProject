# Generated by Django 3.0.4 on 2020-05-13 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200513_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='name',
        ),
    ]
