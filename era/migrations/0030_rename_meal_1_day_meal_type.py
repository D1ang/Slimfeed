# Generated by Django 4.1.4 on 2023-02-05 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('era', '0029_alter_day_meal_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='meal_1',
            new_name='meal_type',
        ),
    ]
