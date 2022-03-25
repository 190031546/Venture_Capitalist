# Generated by Django 3.1.7 on 2021-05-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210511_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('none', 'NONE'), ('M', 'Male'), ('F', 'Female')], default='none', max_length=128),
        ),
        migrations.AddField(
            model_name='customer',
            name='membership',
            field=models.CharField(choices=[('1 years', '1 YEARS'), ('5 years', '5 YEARS')], default='No Membership', max_length=128),
        ),
    ]
