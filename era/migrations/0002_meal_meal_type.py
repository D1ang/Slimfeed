# Generated by Django 4.1.4 on 2023-02-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('era', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
