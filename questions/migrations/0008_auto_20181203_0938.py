# Generated by Django 2.1.3 on 2018-12-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_remove_answer_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]
