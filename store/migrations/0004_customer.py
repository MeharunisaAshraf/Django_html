# Generated by Django 2.1.15 on 2020-12-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201219_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
                ('PhoneNumber', models.IntegerField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
                ('Address1', models.CharField(max_length=100)),
                ('Address2', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('ZipCode', models.IntegerField(max_length=10)),
            ],
        ),
    ]
