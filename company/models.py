from uuid import uuid4

from django.db import models

# Create your models here.
class Company(models.Model):
    logo = models.ImageField(upload_to='media/images', null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=13)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Customer(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="customers",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255, help_text="Name")
    address = models.CharField(max_length=255, help_text="Address")
    tax_number = models.CharField(max_length=13, help_text="Tax Number")
    branch = models.CharField(max_length=5, help_text="Branch")
    email = models.CharField(max_length=255, help_text="Email")
    phone = models.CharField(max_length=255, help_text="Phone")

    def __str__(self):
        return self.name
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="shipping_addresses"
    )
    contact_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    subdistrict = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.customer.name} - {self.contact_name}"

class Province(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name_th}, {self.name_en}"

class District(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    province = models.ForeignKey(
        "Province",
        on_delete=models.CASCADE,
        related_name="districts"
    )

    def __str__(self):
        return f"{self.name_th}, {self.name_en}"

class Subdistrict(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique=True)
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    district = models.ForeignKey(
        "District",
        on_delete=models.CASCADE,
        related_name="subdistricts"
    )

    def __str__(self):
        return f"{self.name_th}, {self.name_en}"