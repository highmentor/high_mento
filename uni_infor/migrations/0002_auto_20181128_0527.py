# Generated by Django 2.1.3 on 2018-11-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_infor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university_review',
            old_name='rating',
            new_name='rating1',
        ),
        migrations.AddField(
            model_name='university_review',
            name='rating2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university_review',
            name='rating3',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]