# Generated by Django 3.1.7 on 2021-05-15 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20210515_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='message',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='subject',
        ),
    ]
