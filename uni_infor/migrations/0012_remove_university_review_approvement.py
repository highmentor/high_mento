# Generated by Django 2.1.3 on 2018-12-03 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_infor', '0011_auto_20181203_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university_review',
            name='approvement',
        ),
    ]
