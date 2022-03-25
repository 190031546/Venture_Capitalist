# Generated by Django 3.1.8 on 2021-05-18 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20210517_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('investor_comment', models.CharField(default='Nothing', max_length=200)),
                ('price', models.CharField(choices=[('1000-10000', '1000-10000'), ('10000-25000', '10000-25000'), ('25000-50000', '25000-50000')], default='No', max_length=128)),
                ('asked_date', models.DateField(auto_now=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer')),
            ],
        ),
    ]
