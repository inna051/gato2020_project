# Generated by Django 5.0.3 on 2024-03-23 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_importantclient_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importantclient',
            name='photo',
        ),
    ]
