# Generated by Django 3.1.7 on 2021-05-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
