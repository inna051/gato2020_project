# Generated by Django 5.0.3 on 2024-03-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
