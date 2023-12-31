# Generated by Django 4.2.2 on 2023-06-30 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmsPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel', models.CharField(choices=[('kavenegar', 'kavenegar'), ('smsdotir', 'smsdotir'), ('webonesms', 'webonesms'), ('melipayamak', 'melipayamak'), ('mediana', 'mediana'), ('ghasedaksms', 'ghasedaksms'), ('farazsms', 'farazsms'), ('niksms', 'niksms'), ('smsone', 'smsone'), ('sapak', 'sapak')], max_length=250)),
                ('api_key', models.CharField(blank=True, max_length=250, null=True)),
                ('username', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receptor', models.CharField(blank=True, max_length=250, null=True)),
                ('msg', models.CharField(blank=True, max_length=250, null=True)),
                ('send_at', models.DateTimeField(auto_now=True)),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.smspanel')),
            ],
        ),
    ]
