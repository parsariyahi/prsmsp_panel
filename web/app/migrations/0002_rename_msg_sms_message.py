# Generated by Django 4.1.4 on 2023-07-01 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sms',
            old_name='msg',
            new_name='message',
        ),
    ]
