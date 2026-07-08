from django.urls import path
from . import views

urlpatterns = [
    path("companies/", views.company_list, name="company_list"),
    path("customers/", views.customer_list, name="customer_list"),
    path(
        "shipping-addresses/",
        views.shipping_address_list,
        name="shipping_address_list",
    ),
]