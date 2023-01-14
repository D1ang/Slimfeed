from django.contrib import admin
from .models import Week, Day, Meal


class MealInline(admin.TabularInline):
    model = Meal


class DayInline(admin.TabularInline):
    model = Day
    inlines = [
        MealInline
    ]





@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    inlines = [
        DayInline,
    ]

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass
