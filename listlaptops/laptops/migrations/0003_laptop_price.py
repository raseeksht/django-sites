# Generated by Django 3.1.4 on 2021-04-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0002_auto_20210418_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='price',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]
