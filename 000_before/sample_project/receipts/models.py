from decimal import Decimal
from django.db import models

class Receipt(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt(id={self.id})"

    def total(self) -> Decimal:
        return sum(item.cost for item in self.item_set.all())

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    description = models.TextField()
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

    def __str__(self):
        return f"Item(id={self.id}, description={self.description}, " \
            f"cost={self.cost})"
