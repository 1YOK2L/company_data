from django.contrib import admin

# Register your models here.
from .models import Company, Customer, ShippingAddress

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("logo", "name", "address", "tax_number", "email", "phone")
    search_fields = ("name", "tax_number", "phone")

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "tax_number", "branch", "email", "phone")
    search_fields = ("name", "tax_number", "phone")

@admin.register(ShippingAddress)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ("contact_name", "phone", "address", "subdistrict", "district", "province", "zip_code")
    search_fields = ("contact_name", "phone")