# Generated by Django 3.2.7 on 2022-05-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yvidh', '0010_font_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='discc',
            field=models.TextField(max_length=3000),
        ),
    ]
