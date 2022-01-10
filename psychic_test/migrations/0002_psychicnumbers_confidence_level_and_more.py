# Generated by Django 4.0.1 on 2022-01-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychic_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychicnumbers',
            name='confidence_level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usernumbers',
            name='number',
            field=models.SmallIntegerField(verbose_name='Число'),
        ),
    ]