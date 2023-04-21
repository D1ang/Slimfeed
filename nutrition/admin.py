from django.contrib import admin
from .models import Product, Unit, ProductGroup


class ProductAdmin(admin.ModelAdmin):
    pass


class UnitAdmin(admin.ModelAdmin):
    pass


class ProductGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
