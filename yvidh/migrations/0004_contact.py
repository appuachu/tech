# Generated by Django 3.2.7 on 2022-05-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yvidh', '0003_auto_20220526_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=200)),
                ('time', models.TimeField()),
                ('Phone', models.IntegerField()),
                ('Email', models.TextField(max_length=400)),
            ],
        ),
    ]
