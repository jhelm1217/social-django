# Generated by Django 5.0.6 on 2024-06-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_social', '0008_alter_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
