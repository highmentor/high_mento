# Generated by Django 2.1.3 on 2018-12-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_infor', '0010_university_review_approvement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university_review',
            name='approvement',
            field=models.TextField(),
        ),
    ]
