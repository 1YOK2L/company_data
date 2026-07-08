# from django.contrib import admin

# # Register your models here.
# from .models import Company, Customer, ShippingAddress

# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ("logo", "name", "address", "tax_number", "email", "phone")
#     search_fields = ("name", "tax_number", "phone")

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ("name", "address", "tax_number", "branch", "email", "phone")
#     search_fields = ("name", "tax_number", "phone")

# @admin.register(ShippingAddress)
# class ShippingAdmin(admin.ModelAdmin):
#     list_display = ("contact_name", "phone", "address", "subdistrict", "district", "province", "zip_code")
#     search_fields = ("contact_name", "phone")

from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import Company, Customer, ShippingAddress


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "tax_number",
        "branch",
        "email",
        "phone",
    )
    search_fields = ("name", "tax_number", "phone")

    actions = ["export_report"]

    @admin.action(description="Export customer report")
    def export_report(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="customer_report.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "Customer",
            "Tax Number",
            "Branch",
            "Phone",
            "Shipping Contact",
            "Shipping Address",
        ])

        for customer in queryset:
            addresses = ShippingAddress.objects.filter(customer=customer)

            if addresses.exists():
                for addr in addresses:
                    writer.writerow([
                        customer.name,
                        customer.tax_number,
                        customer.branch,
                        customer.phone,
                        addr.contact_name,
                        addr.address,
                    ])
            else:
                writer.writerow([
                    customer.name,
                    customer.tax_number,
                    customer.branch,
                    customer.phone,
                    "",
                    "",
                ])

        return response