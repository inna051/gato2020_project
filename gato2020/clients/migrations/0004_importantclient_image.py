# Generated by Django 5.0.3 on 2024-03-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_remove_importantclient_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='importantclient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='client_images/'),
        ),
    ]
