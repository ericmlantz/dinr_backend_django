# Generated by Django 4.0.4 on 2022-05-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinr', '0002_alter_restaurant_rest_apt_alter_user_apt_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='matches',
            field=models.ManyToManyField(blank=True, to='dinr.restaurant'),
        ),
    ]
