# Generated by Django 4.2.7 on 2023-11-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='is_active_setting',
            field=models.BooleanField(default=False, verbose_name='فعال / غیر فعال'),
        ),
    ]
