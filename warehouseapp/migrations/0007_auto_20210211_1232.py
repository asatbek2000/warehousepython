# Generated by Django 3.1.6 on 2021-02-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouseapp', '0006_auto_20210211_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userlist',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
