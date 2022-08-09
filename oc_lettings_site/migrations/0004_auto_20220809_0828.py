# Generated by Django 4.0.6 on 2022-08-09 06:28
"""
Created manually to remove the FK fields of the old models and eventually remove the old models.
This migrations does NOT revert.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0003_alter_address_id_alter_letting_id_alter_profile_id_and_more'),
    ]

    operations = [
        migrations.RemoveField('letting', 'address'),
        migrations.RemoveField('profile', 'user'),
        migrations.DeleteModel('profile'),
        migrations.DeleteModel('letting'),
        migrations.DeleteModel('address'),
    ]
