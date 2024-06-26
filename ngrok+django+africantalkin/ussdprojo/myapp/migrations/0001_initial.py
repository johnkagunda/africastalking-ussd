# Generated by Django 5.0.2 on 2024-03-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('average_capital', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idea', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
