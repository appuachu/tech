# Generated by Django 3.2.7 on 2022-05-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yvidh', '0011_alter_event_discc'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_contact',
            field=models.IntegerField(default='123', max_length=10),
            preserve_default=False,
        ),
    ]
