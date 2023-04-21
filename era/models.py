from django.db import models, transaction
from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver
from nutrition.models import Product


class Week(models.Model):
    def get_last_week():
        current_last_week = Week.objects.all().aggregate(last_week=Max('week'))['last_week']
        return current_last_week + 1 if current_last_week else 1

    week = models.PositiveIntegerField(default=get_last_week)

    def __str__(self):
        return f'Week {self.week}'


class Day(models.Model):
    DAYS_OF_WEEK = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day_name = models.CharField(max_length=10, choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.day_name


class Meal(models.Model):
    MEAL_OF_DAY = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('diner', 'Diner'),
        ('snack', 'Snack'),
    )
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=10, choices=MEAL_OF_DAY)
    product = models.ManyToManyField(Product)
    
    def __str__(self):
        return self.description
