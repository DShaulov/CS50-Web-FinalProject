# Generated by Django 3.0.4 on 2020-06-15 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20200614_2006'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DuplicateCounter',
            new_name='ProductCounter',
        ),
    ]
