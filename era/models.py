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
        return f"Week {self.week}"


class Meal(models.Model):
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description


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
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    meal_type = models.ManyToManyField(Meal)

    def __str__(self):
        return self.day
