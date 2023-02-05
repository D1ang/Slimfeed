from django.contrib import admin
from django.db.models import Max
from .models import Week, Day, Meal
from nested_admin import NestedTabularInline, NestedModelAdmin


class DayInline(admin.TabularInline):
    model = Day
    extra = 7
    max_num = 7
    can_delete = False
    show_change_link = False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    """
    if the object doesn't have a primary key,
    'save_model' will set the week to the current maximum week +1,
    otherwise, it will keep the value as it is.
    """

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            current_max_week = Week.objects.all().aggregate(max_week=Max('week'))['max_week']
            obj.week = current_max_week + 1 if current_max_week else 1
        super().save_model(request, obj, form, change)

    inlines = [DayInline]
    ordering = ['week']


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass
