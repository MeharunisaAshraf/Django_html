# Generated by Django 2.1.15 on 2020-12-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201225_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Lname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]