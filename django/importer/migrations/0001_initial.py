# Generated by Django 3.2.20 on 2024-01-10 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid_upload_path.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labelbase', '0010_alter_label_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_type', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to=uuid_upload_path.storage.upload_to)),
                ('labelbase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labelbase.labelbase')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]