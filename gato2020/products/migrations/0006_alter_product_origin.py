# Generated by Django 5.0.3 on 2024-04-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_intensity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='origin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
