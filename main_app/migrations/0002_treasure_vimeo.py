# Generated by Django 2.2.1 on 2019-05-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='vimeo',
            field=models.CharField(default='http://www.vimeo.com', max_length=100),
        ),
    ]