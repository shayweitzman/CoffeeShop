# Generated by Django 4.0.1 on 2022-01-20 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_alter_client_is_vip'),
        ('Tables', '0005_alter_table_unavailabday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableorder',
            name='clients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.client'),
        ),
        migrations.AlterField(
            model_name='tableorder',
            name='tables',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tables.table'),
        ),
    ]