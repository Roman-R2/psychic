# Generated by Django 4.0.1 on 2022-01-10 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psychic_test', '0006_usernumbers_is_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychicnumbers',
            name='is_checked',
        ),
        migrations.RemoveField(
            model_name='usernumbers',
            name='is_checked',
        ),
    ]