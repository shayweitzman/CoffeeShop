# Generated by Django 3.2.10 on 2022-01-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quatities',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.RemoveField(
            model_name='order',
            name='menuObjs',
        ),
        migrations.AddField(
            model_name='order',
            name='menuObjs',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]