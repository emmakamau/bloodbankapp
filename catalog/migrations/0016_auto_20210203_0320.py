# Generated by Django 3.1.5 on 2021-02-03 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('catalog', '0015_hospital_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='group',
        ),
        migrations.AddField(
            model_name='hospital',
            name='group',
            field=models.OneToOneField(choices=[('Hospital', 'Hospital'), ('Donor', 'Donor')], null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]