# Generated by Django 2.2.1 on 2019-05-15 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('thelink', models.CharField(max_length=100)),
            ],
        ),
    ]
