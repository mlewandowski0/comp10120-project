# Generated by Django 3.1.6 on 2021-03-08 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REST', '0005_remove_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]