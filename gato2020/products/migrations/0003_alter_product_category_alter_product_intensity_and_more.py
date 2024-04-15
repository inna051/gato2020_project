# Generated by Django 5.0.3 on 2024-04-01 17:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_description_remove_product_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='intensity',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='package_weight',
            field=models.DecimalField(decimal_places=3, max_digits=4),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]