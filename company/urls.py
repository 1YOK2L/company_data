from django.urls import path
from . import views

urlpatterns = [
    path(
        "shipping-addresses/",
        views.shipping_address_list,
        name="shipping_address_list",
    ),
]