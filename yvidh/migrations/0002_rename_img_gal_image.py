# Generated by Django 3.2.7 on 2022-05-26 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yvidh', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gal',
            old_name='img',
            new_name='image',
        ),
    ]
