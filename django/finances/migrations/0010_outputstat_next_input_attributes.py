# Generated by Django 3.2.24 on 2024-03-29 17:38

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0009_alter_outputstat_last_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='outputstat',
            name='next_input_attributes',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
