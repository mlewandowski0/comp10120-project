# Generated by Django 3.1.6 on 2021-03-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REST', '0009_auto_20210310_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='REST.UserProfile'),
        ),
    ]
