# Generated by Django 3.1.4 on 2021-02-05 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_remove_hospital_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='pintsavailable',
        ),
        migrations.AddField(
            model_name='pintsavailable',
            name='hospital',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.hospital'),
        ),
    ]