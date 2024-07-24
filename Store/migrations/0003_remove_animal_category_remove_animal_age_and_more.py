# Generated by Django 5.0.6 on 2024-07-17 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='category',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='age',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='description',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='price',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='scientific_name',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='traits',
        ),
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
