# Generated by Django 3.0.4 on 2020-05-07 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_electronic_image_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.Electronic')),
                ('image', models.ImageField(upload_to='')),
                ('technical_details', models.TextField(blank=True)),
            ],
            bases=('store.electronic',),
        ),
        
        migrations.DeleteModel(
            name='Computer',
        ),
        migrations.DeleteModel(
            name='Headphones',
        ),
        migrations.DeleteModel(
            name='Television',
        ),
    ]
