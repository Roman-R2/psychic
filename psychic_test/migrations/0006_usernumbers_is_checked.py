# Generated by Django 4.0.1 on 2022-01-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychic_test', '0005_psychicnumbers_is_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernumbers',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
