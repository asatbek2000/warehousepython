# Generated by Django 3.1.6 on 2021-02-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouseapp', '0005_auto_20210210_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'main_branch'), (2, 'custom_branch'), (3, 'admin')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='userlist',
            name='role',
        ),
        migrations.AddField(
            model_name='userlist',
            name='role',
            field=models.ManyToManyField(to='warehouseapp.Role'),
        ),
    ]
