# Generated by Django 4.0.1 on 2022-01-12 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='spacielObj',
        ),
        migrations.AlterField(
            model_name='menuobj',
            name='category',
            field=models.ManyToManyField(to='Menu.categoryMenu'),
        ),
    ]