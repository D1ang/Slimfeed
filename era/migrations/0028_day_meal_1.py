# Generated by Django 4.1.4 on 2023-02-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_alter_product_unit'),
        ('era', '0027_remove_day_meal_1_remove_week_monday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='meal_1',
            field=models.ManyToManyField(to='nutrition.product'),
        ),
    ]
