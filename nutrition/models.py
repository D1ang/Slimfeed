from django.db import models


class Unit(models.Model):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description


class ProductGroup(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    product = models.CharField(max_length=150)
    amount = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)

    def __str__(self):
        if self.unit is None:
            return f"{self.amount} {self.product}"
        return f"{self.amount} {self.unit} {self.product}"
