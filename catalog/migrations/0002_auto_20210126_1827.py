# Generated by Django 3.1.5 on 2021-01-26 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='bloodgroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.bloodgroup'),
        ),
        migrations.AddField(
            model_name='donor',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.location'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='bloodgroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.bloodgroup'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.location'),
        ),
    ]
