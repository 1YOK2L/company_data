from django.shortcuts import render
from .models import Company, Customer, ShippingAddress


def company_list(request):
    companies = Company.objects.all()

    return render(
        request,
        "company/company_list.html",
        {
            "companies": companies,
        },
    )


def customer_list(request):
    customers = Customer.objects.select_related("company")

    return render(
        request,
        "customer/customer_list.html",
        {
            "customers": customers,
        },
    )


def shipping_address_list(request):
    shipping_addresses = ShippingAddress.objects.select_related(
        "customer",
        "customer__company",
    )

    return render(
        request,
        "shipping/shipping_address_list.html",
        {
            "shipping_addresses": shipping_addresses,
        },
    )