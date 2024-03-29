# Generated by Django 3.2.5 on 2021-07-03 20:40

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
                ('name', models.CharField(max_length=200, unique=True)),
                ('slag', models.SlugField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryOption', models.CharField(max_length=200)),
                ('deliveryPrice', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Deliveries',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('preview', models.TextField()),
                ('content', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('images', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('article', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('final_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('preview', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'ProductSizes',
            },
        ),
        migrations.CreateModel(
            name='ProductsOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
            ],
            options={
                'verbose_name_plural': 'ProductsOrders',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='products/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ecommerce.product')),
            ],
            options={
                'verbose_name_plural': 'ProductImages',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(related_name='prodSize', to='ecommerce.ProductSize'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('agree', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ecommerce.delivery')),
                ('productsOrder', models.ManyToManyField(related_name='productsOrder', to='ecommerce.ProductsOrder')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='news/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('news', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.news')),
            ],
            options={
                'verbose_name_plural': 'NewsImages',
            },
        ),
    ]
