# Generated by Django 3.1.3 on 2021-11-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20211107_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
