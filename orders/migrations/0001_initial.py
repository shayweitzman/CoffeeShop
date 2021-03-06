# Generated by Django 3.2.10 on 2022-01-21 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuObjs', models.CharField(max_length=2000, null=True)),
                ('quatities', models.CharField(max_length=2000, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('alreadyPrepared', models.BooleanField(default=False)),
                ('paymentMethod', models.CharField(max_length=20, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.client')),
            ],
        ),
    ]
