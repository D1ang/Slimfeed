# Generated by Django 4.1.4 on 2023-02-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('era', '0022_remove_day_meal_day_meals'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='meal_1',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
