from django.contrib import admin
from .models import Week, Day



class DayInline(admin.TabularInline):
    """
    Inline upload attachment field
    for the item admin
    """
    model = Day
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    inlines = [
        DayInline,
    ]


admin.site.register(Week, ItemAdmin)
