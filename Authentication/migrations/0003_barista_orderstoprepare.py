# Generated by Django 3.2.10 on 2022-01-20 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_alter_client_is_vip'),
    ]

    operations = [
        migrations.AddField(
            model_name='barista',
            name='ordersToPrepare',
            field=models.IntegerField(default=0),
        ),
    ]
