# Generated by Django 3.2.8 on 2021-10-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('item', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]