# Generated by Django 2.1.15 on 2020-12-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_customer_address2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Address1',
            new_name='Address',
        ),
        migrations.AlterField(
            model_name='customer',
            name='PhoneNumber',
            field=models.IntegerField(),
        ),
    ]
