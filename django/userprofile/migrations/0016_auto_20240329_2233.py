# Generated by Django 3.2.24 on 2024-03-29 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0015_alter_profile_use_sentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='electrum_hostname_test',
            field=models.CharField(blank=True, default='testnet.qtornado.com', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='electrum_ports_test',
            field=models.CharField(blank=True, default='t51001', max_length=6),
        ),
    ]
