from django.contrib import admin
from django.shortcuts import render

# Register your models here.
from .models import Company, Customer, District, ShippingAddress, Province, Subdistrict

@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    customers = []
    return render(
        request,
        "customer/customer_list.html",
        {"customers": customers},
    )

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
    actions = [make_published]

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("id", "name_th", "name_en")
    search_fields = ("name_th", "name_en")

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name_th", "name_en")
    search_fields = ("name_th", "name_en")

@admin.register(Subdistrict)
class SubdistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name_th", "name_en")
    search_fields = ("name_th", "name_en")