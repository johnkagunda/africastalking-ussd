# Generated by Django 5.0.2 on 2024-03-27 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_businessidea_competitive_advantage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessidea',
            name='competitive_advantage',
        ),
        migrations.RemoveField(
            model_name='businessidea',
            name='location',
        ),
        migrations.RemoveField(
            model_name='businessidea',
            name='marketing_strategy',
        ),
        migrations.RemoveField(
            model_name='businessidea',
            name='potential_challenges',
        ),
        migrations.RemoveField(
            model_name='businessidea',
            name='resources_needed',
        ),
        migrations.RemoveField(
            model_name='businessidea',
            name='target_audience',
        ),
    ]
