# Generated by Django 2.1.3 on 2018-12-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_infor', '0002_auto_20181128_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='uni_id',
            field=models.CharField(max_length=100),
        ),
    ]
