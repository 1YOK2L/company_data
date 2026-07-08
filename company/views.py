from django.shortcuts import render
from .models import Company, Customer, ShippingAddress

def company_list(request):
    # companies = [
    #     {
    #         "name": "Tech Solutions Ltd.",
    #         "address": "123 Main Street, New York, NY",
    #         "tax_number": "TX123456789",
    #         "email": "info@techsolutions.com",
    #         "phone": "+1 555-123-4567",
    #     },
    #     {
    #         "name": "Green Energy Inc.",
    #         "address": "45 Oak Avenue, Los Angeles, CA",
    #         "tax_number": "TX987654321",
    #         "email": "contact@greenenergy.com",
    #         "phone": "+1 555-987-6543",
    #     },
    #     {
    #         "name": "Blue Ocean Trading",
    #         "address": "78 Harbor Road, Miami, FL",
    #         "tax_number": "TX456789123",
    #         "email": "sales@blueocean.com",
    #         "phone": "+1 555-456-7890",
    #     },
    #     {
    #         "name": "Future Innovations",
    #         "address": "900 Silicon Blvd, Austin, TX",
    #         "tax_number": "TX741852963",
    #         "email": "hello@futureinnovations.com",
    #         "phone": "+1 555-741-8529",
    #     },
    #     {
    #         "name": "Global Logistics",
    #         "address": "22 Commerce Park, Chicago, IL",
    #         "tax_number": "TX369258147",
    #         "email": "support@globallogistics.com",
    #         "phone": "+1 555-369-2581",
    #     },
    # ]
    companies = Company.objects.all()

    return render(request, "company/company_list.html", {"companies": companies})


def customer_list(request):
    customers = Customer.objects.select_related("company").all()
    return render(
        request,
        "customer/customer_list.html",
        {"customers": customers},
    )

def shipping_address_list(request):
    shipping_addresses = ShippingAddress.objects.select_related(
        "customer",
        "customer__company"
    )

    return render(
        request,
        "shipping/shipping_address_list.html",
        {
            "shipping_addresses": shipping_addresses
        },
    )

# PS C:\Users\Asus\data> python manage.py shell                                                                                
# 9 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from company.models import Company, Customer, ShippingAddress
# >>> 
# >>> company = Company.objects.create(name="Tech Solutions Ltd.", address="123 Main Street, New York, NY", tax_number="TX123456789", email="info@techsolutions.com", phone="+1 555-123-4567")                                           
# >>> john = Customer.objects.create(company = company, name="Tech Solutions Ltd.", address="Los Angeles, CA", tax_number="TX10150814", branch="00001", email="johndoe@gmail.com", phone="+1 555-067-6767")
# >>> john = Customer.objects.create(company = company, name="John Doe", address="Los Angeles, CA", tax_number="TX10150814", branch="00001", email="johndoe@gmail.com", phone="+1 555-067-6767")           
# >>> Customer.objects.get(name="Tech Solutions Ltd.").delete()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\Asus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\Users\Asus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\db\models\query.py", line 636, in get
#     raise self.model.MultipleObjectsReturned(
#     ...<5 lines>...
#     )
# company.models.Customer.MultipleObjectsReturned: get() returned more than one Customer -- it returned 3!
# >>> Customer.objects.all().delete()                          
# (4, {'company.Customer': 4})
# >>> john = Customer.objects.create(company = company, name="John Doe", address="Los Angeles, CA", tax_number="TX10150814", branch="00001", email="johndoe@gmail.com", phone="+1 555-067-6767")
# >>> jane = Customer.objects.create(company = company, name="Jane Doe", address="San Francisco, CA", tax_number="TX10011405", branch="00002", email="janelovesjohn@gmail.com", phone="+1 555-069-0420") 
# >>> ShippingAddress.objects.create(customer=john,contact_name="John Doe",phone="+1 555-067-6767",address="69/420",subdistrict="ASDF",district="JKL",province="GH",zip_code="90001",)
# <ShippingAddress: John Doe - John Doe>
# >>> ShippingAddress.objects.create(customer=jane,contact_name="Jane Doe",phone="+1 555-069-0420",address="69/420",subdistrict="ASDF",district="JKL",province="GH",zip_code="90001",)
# <ShippingAddress: Jane Doe - Jane Doe>
# >>> 20+20+20+7                     
# 67
# >>> company = Company.objects.create(name="depa", address="DEPA Building A 234/431 Soi Ladprao 10, Ladprao Rd., Jomphol, Chatuchak, Bangkok, 10900", tax_number="TX123456789", email="spwd@gmail.com", phone="+66 88-227-2777")
# >>> spwd = Customer.objects.create(company = company, name="Suphawadee", address="Bangkok, Thailand", tax_number="TX19162304", branch="00001", email="spwd@gmail.com", phone="+66 88-227-2777")
# >>> ShippingAddress.objects.create(customer=spwd,contact_name="Suphawadee (Finance)",phone="+66 88-227-2777",address="234/431",subdistrict="Jomphol",district="Chatuchak",province="Bangkok",zip_code="10900",)
# <ShippingAddress: Suphawadee - Suphawadee (Finance)>
# >>> company = Company.objects.create(name="Sea Sun Sand Resort and Spa", address="Patong, Phuket, Thailand", tax_number="TX254", email="s3phuket.com", phone="+66 95-292-9966")
# >>> john = Customer.objects.create(company = company, name="Saroch Tantipatanaseri", address="Patong, Phuket, Thailand", tax_number="TX254", branch="254", email="sarocht1@outlook.com", phone="+66 95-292-9966")
# >>> ShippingAddress.objects.create(customer=john,contact_name="Saroch Tantipatanaseri",phone="+1 555-067-6767",address="68/15 Village 7 Vichitsongkram Rd.",subdistrict="Kathu",district="Kathu",province="Phuket",zip_code="83120",)
# <ShippingAddress: Saroch Tantipatanaseri - Saroch Tantipatanaseri>
# >>> ShippingAddress.objects.get(contact_name="Saroch Tantipatanaseri").delete()
# (1, {'company.ShippingAddress': 1})
# >>> ShippingAddress.objects.create(customer=john,contact_name="Saroch Tantipatanaseri",phone="+66 95-292-9966",address="68/15 Village 7 Vichitsongkram Rd.",subdistrict="Kathu",district="Kathu",province="Phuket",zip_code="83120",)
# <ShippingAddress: Saroch Tantipatanaseri - Saroch Tantipatanaseri>
# >>> 