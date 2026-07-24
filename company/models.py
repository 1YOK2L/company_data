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
    
# class ShippingAddress(models.Model):
#     id = models.UUIDField(default=uuid4, editable=False, primary_key=True)

#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE,
#         related_name="shipping_addresses"
#     )

#     contact_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     dept = models.CharField(max_length=255, null=True, blank=True) # add independent company on the shipping section of the django admin page
#     address = models.CharField(max_length=255)
#     alley = models.CharField(max_length=255, blank=True,null=True)
#     road = models.CharField(max_length=255, blank=True,null=True)
#     subdistrict = models.ForeignKey(
#         "Subdistrict",
#         on_delete=models.PROTECT,
#         related_name="shipping_addresses"
#     )

#     def __str__(self):
#         return f"{self.customer.name} - {self.contact_name}"

#     @property
#     def district(self):
#         return self.subdistrict.district

#     @property
#     def province(self):
#         return self.subdistrict.district.province

#     @property
#     def zip_code(self):
#         return self.subdistrict.zip_code
    
#     @property
#     def formatted_location(self):
#         if self.province.name_th == "กรุงเทพมหานคร":
#             if self.district.name_th[:3] == "เขต":
#                 return (
#                     f"แขวง{self.subdistrict.name_th} "
#                     f"{self.district.name_th} "
#                     f"{self.province.name_th}"
#                 )
#             else:
#                 return (
#                     f"แขวง{self.subdistrict.name_th} "
#                     f"เขต{self.district.name_th} "
#                     f"{self.province.name_th}"
#                 )

#         return (
#             f"ต.{self.subdistrict.name_th} "
#             f"อ.{self.district.name_th} "
#             f"จ.{self.province.name_th}"
#         )

class ShippingAddress(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="shipping_addresses"
    )

    contact_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    dept = models.CharField(max_length=255, blank=True, null=True)

    address = models.CharField(max_length=255)

    alley = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Alley (ซอย)"
    )

    road = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Road (ถนน)"
    )

    subdistrict = models.ForeignKey(
        "Subdistrict",
        on_delete=models.PROTECT,
        related_name="shipping_addresses"
    )

    def __str__(self):
        return f"{self.customer.name} - {self.contact_name}"

    @property
    def district(self):
        return self.subdistrict.district

    @property
    def province(self):
        return self.subdistrict.district.province

    @property
    def zip_code(self):
        return self.subdistrict.zip_code

    @property
    def formatted_location(self):
        location = []

        if self.alley:
            location.append(f"ซ.{self.alley}")

        if self.road:
            location.append(f"ถ.{self.road}")

        if self.province.name_th == "กรุงเทพมหานคร":
            location.append(f"แขวง{self.subdistrict.name_th}")

            if self.district.name_th.startswith("เขต"):
                location.append(self.district.name_th)
            else:
                location.append(f"เขต{self.district.name_th}")

            location.append(self.province.name_th)
        else:
            location.extend([
                f"ต.{self.subdistrict.name_th}",
                f"อ.{self.district.name_th}",
                f"จ.{self.province.name_th}",
            ])

        return " ".join(location)

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
    zip_code = models.CharField(max_length=5)
    district = models.ForeignKey(
        "District",
        on_delete=models.CASCADE,
        related_name="subdistricts"
    )
    def __str__(self):
        return f"{self.name_th} • {self.district.name_th} • {self.district.province.name_th}"
    
# add alley/road field in django admin and provide the complete code of files edited