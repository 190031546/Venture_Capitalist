# Generated by Django 3.1.7 on 2021-05-10 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('App', 'App'), ('Web', 'Web')], max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Published', 'Published'), ('Working on It', 'Working on It'), ('Not Published', 'Not Published')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
                ('Applications', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.applications')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer')),
            ],
        ),
    ]
