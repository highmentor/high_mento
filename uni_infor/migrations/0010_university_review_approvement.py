# Generated by Django 2.1.3 on 2018-12-03 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_infor', '0009_auto_20181203_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='university_review',
            name='approvement',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
