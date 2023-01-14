from django.contrib import admin
from .models import Product, Unit


class ProductAdmin(admin.ModelAdmin):
    pass


class UnitAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Unit, UnitAdmin)
