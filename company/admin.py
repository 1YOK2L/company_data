from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, reverse

from .models import Company, Customer, ShippingAddress


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("logo", "name", "address", "tax_number", "email", "phone")
    search_fields = ("name", "tax_number", "phone")


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

    def export_report(self, request, queryset):
        if queryset.count() != 1:
            self.message_user(
                request,
                "Please select exactly one customer."
            )
            return

        customer = queryset.first()

        return HttpResponseRedirect(
            reverse(
                "admin:customer-export-report",
                args=[customer.pk]
            )
        )

    export_report.short_description = "Export Report"

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                "export-report/<int:customer_id>/",
                self.admin_site.admin_view(self.export_report_view),
                name="customer-export-report",
            ),
        ]

        return custom_urls + urls

    def export_report_view(self, request, customer_id):
        from django.shortcuts import render, get_object_or_404

        customer = get_object_or_404(Customer, pk=customer_id)
        addresses = ShippingAddress.objects.all()

        return render(
            request,
            "admin/export_report.html",
            {
                "customer": customer,
                "addresses": addresses,
            },
        )


@admin.register(ShippingAddress)
class ShippingAdmin(admin.ModelAdmin):
    list_display = (
        "contact_name",
        "phone",
        "address",
        "subdistrict",
        "district",
        "province",
        "zip_code",
    )
    search_fields = ("contact_name", "phone")