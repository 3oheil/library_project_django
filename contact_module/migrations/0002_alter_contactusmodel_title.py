# Generated by Django 4.2.7 on 2023-11-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='title',
            field=models.CharField(max_length=200, verbose_name='موضوع'),
        ),
    ]
