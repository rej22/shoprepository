# Generated by Django 4.1.5 on 2023-01-27 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('CategoryImage', models.ImageField(blank=True, upload_to='category_img')),
                ('CategoryDescription', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('categoryName',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('productImage', models.ImageField(blank=True, upload_to='product_img')),
                ('productDescription', models.TextField(blank=True)),
                ('productAvailable', models.BooleanField(default=True)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('productStock', models.IntegerField()),
                ('productCreatedAt', models.DateField(auto_now_add=True)),
                ('productUpdateAt', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop02.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('productName',),
            },
        ),
    ]
