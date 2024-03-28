# Generated by Django 5.0.2 on 2024-03-28 10:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_user_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]