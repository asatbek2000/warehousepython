# Generated by Django 3.1.6 on 2021-02-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
