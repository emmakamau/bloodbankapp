# Generated by Django 3.1.4 on 2021-02-05 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_auto_20210203_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='group',
        ),
    ]
