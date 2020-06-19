# Generated by Django 3.0.4 on 2020-06-12 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_book_product_image_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='store.Product')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.User')),
            ],
        ),
    ]
