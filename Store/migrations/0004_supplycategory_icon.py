# Generated by Django 5.0.6 on 2024-08-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_supplycategory_supplies'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplycategory',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='supply_categories/'),
        ),
    ]
