# Generated by Django 3.1.6 on 2021-02-10 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouseapp', '0004_userlist_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlist',
            old_name='name',
            new_name='username',
        ),
    ]
