# Generated by Django 4.2.7 on 2023-11-11 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0004_article_auther'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2023, 11, 11), verbose_name='تاریخ انتشار'),
            preserve_default=False,
        ),
    ]
