# Generated by Django 4.0.6 on 2022-08-06 12:39
# this script does NOT revert
from django.db import migrations


def move_data(apps, schema_editor):

    # if the old model of the old app still exists
    try:
        AddressOcLettings = apps.get_model("oc_lettings_site", "Address")
        AddressOcLettings = apps.get_model("oc_lettings_site", "Address")
        AddressLettings = apps.get_model("lettings", "Address")
        LettingLettings = apps.get_model("lettings", "Letting")
        LettingOcLettings = apps.get_model("oc_lettings_site", "Letting")
    except LookupError:
        return

    for address in AddressOcLettings.objects.all():
        address_lettings = AddressLettings(
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            country_iso_code=address.country_iso_code,
        )
        address_lettings.save()
        for letting in LettingOcLettings.objects.filter(address=address):
            letting_lettings = LettingLettings(
                title=letting.title,
                address=address_lettings
            )
            letting_lettings.save()


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ("oc_lettings_site", "0003_alter_address_id_alter_letting_id_alter_profile_id_and_more"),
    ]

    operations = [
        migrations.RunPython(move_data),
    ]
