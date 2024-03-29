# Generated by Django 3.2.5 on 2021-07-04 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_productimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.ImageField(upload_to='products/', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ecommerce.product'),
        ),
    ]
