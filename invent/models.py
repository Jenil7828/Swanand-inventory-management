import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
LOCATION_CHOICES = [
    ("Lonavala", "Lonavala"),
    ("Pune", "Pune"),
    ("Pune2", "Pune2"),
    ("Nashik", "Nashik"),
    ("Girgaon", "Girgaon"),
    ("Mindgym", "Mindgym"),
    ("Kharghar", "Kharghar"),
]

class CustomUser(AbstractUser):
    is_super_admin = models.BooleanField(default=False)
    is_location_admin = models.BooleanField(default=False)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_super_admin:
            self.is_superuser = True
            self.is_staff = True
        elif self.is_location_admin:
            self.is_staff = True
        else:
            # Optional: Reset if neither
            self.is_superuser = False
            self.is_staff = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({'Super Admin' if self.is_super_admin else 'Location Admin' if self.is_location_admin else 'Employee'})"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Company(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ₹{self.cost}"



class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} @ {self.location} ({self.quantity})"


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = f'TXN{uuid.uuid4().int % 10**10}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.transaction_id} on {self.date.strftime('%Y-%m-%d %H:%M')}"

class StockEntry(models.Model):
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        related_name='entries',
        null=True,  # ✅ allow nulls during staging
        blank=True  # ✅ allows forms to skip this field
    )
    date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # ✅ Correct
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    staged = models.BooleanField(default=True)  # 🆕
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    @property
    def total_cost(self):
        return self.quantity * self.product.cost




class StockTransfer(models.Model):
    transaction_id = models.CharField(max_length=20, unique=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    to_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = f"TRF{int(timezone.now().timestamp())}"
        super().save(*args, **kwargs)

        # Update Inventory: Deduct from from_location
        from_inventory, _ = Inventory.objects.get_or_create(product=self.product, location=self.from_location)
        to_inventory, _ = Inventory.objects.get_or_create(product=self.product, location=self.to_location)

        if from_inventory.quantity < self.quantity:
            raise ValueError("Not enough stock to transfer.")

        from_inventory.quantity -= self.quantity
        from_inventory.save()

        to_inventory.quantity += self.quantity
        to_inventory.save()

    def __str__(self):
        return f"{self.product.name} | {self.from_location} ➜ {self.to_location} | Qty: {self.quantity}"




# import uuid
# from django.db import models
# from django.utils import timezone
#
# # Create your models here.
# class Company(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=100, blank=True)
#
#     def __str__(self):
#         return self.name
#
# class Product(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return f"{self.name} - ₹{self.cost}"
#
# class StockEntry(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     add_stock_id = models.CharField(max_length=20, unique=True, editable=False)
#
#     def save(self, *args, **kwargs):
#         if not self.add_stock_id:
#             self.add_stock_id = f"ADD{int(timezone.now().timestamp())}"
#         super().save(*args, **kwargs)
#
#         # Update Inventory stock
#         inventory, _ = Inventory.objects.get_or_create(product=self.product, location="Lonavala")  # or default
#         inventory.quantity += self.quantity
#         inventory.save()
#
#     @property
#     def total_cost(self):
#         return self.quantity * self.product.cost
#
#
#
# LOCATION_CHOICES = [
#     ("Lonavala", "Lonavala"),
#     ("Pune", "Pune"),
#     ("Pune2", "Pune2"),
#     ("Nashik", "Nashik"),
#     ("Girgaon", "Girgaon"),
#     ("Mindgym", "Mindgym"),
#     ("Kharghar", "Kharghar"),
# ]
#
# class Inventory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
#     quantity = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return f"{self.product.name} @ {self.location} ({self.quantity})"
#
#
# class StockTransfer(models.Model):
#     transaction_id = models.CharField(max_length=20, unique=True, editable=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     from_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
#     to_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
#     quantity = models.PositiveIntegerField()
#     timestamp = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return f"{self.product.name} | {self.from_location} ➜ {self.to_location} | Qty: {self.quantity}"
#




"""
class StockTransfer(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
"""