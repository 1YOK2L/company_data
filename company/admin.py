from django.contrib import admin
from django.shortcuts import render, get_object_or_404
from django.urls import path

# Register your models here.
from .models import Company, Customer, District, ShippingAddress, Province, Subdistrict

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "logo", "address", "tax_number", "email", "phone")
    search_fields = ("name", "tax_number", "phone")

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "tax_number", "branch", "email", "phone")
    search_fields = ("name", "tax_number", "phone")

@admin.register(ShippingAddress)
class ShippingAdmin(admin.ModelAdmin):
    list_display = (
        "contact_name",
        "phone",
        "alley",
        "road",
        "address",
        "subdistrict",
        "district",
        "province",
        "zip_code",
    )

    search_fields = (
            "contact_name",
            "phone",
            "address",
            "alley",
            "road",
        )

    autocomplete_fields = ["subdistrict"]
    fields = (
            "customer",
            "contact_name",
            "phone",
            "dept",
            "address",
            "alley",
            "road",
            "subdistrict",
        )
    change_form_template = "admin/company/shippingaddress/change_form.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<uuid:pk>/print/",
                self.admin_site.admin_view(self.print_letter),
                name="company_shippingaddress_print",
            ),
            path(
                "<uuid:pk>/print-a4/",
                self.admin_site.admin_view(self.print_a4),
                name="company_shippingaddress_print_a4",
            ),
        ]
        return custom_urls + urls

    def print_letter(self, request, pk):
        shipping = ShippingAddress.objects.filter(pk=pk)

        return render(
            request,
            "shipping/shipping_address_list.html",
            {
                "shipping_addresses": shipping,
            },
        )

    def print_a4(self, request, pk):
        shipping = ShippingAddress.objects.filter(pk=pk)

        return render(
            request,
            "shipping/shipping_address_list_a4.html",
            {
                "shipping_addresses": shipping,
            },
        )

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

@admin.action(description="Print Shipping Labels")
def print_labels(modeladmin, request, queryset):
    return render(
        request,
        "shipping/shipping_address_list.html",
        {
            "shipping_addresses": queryset,
        },
    )