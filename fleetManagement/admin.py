from django.contrib import admin
from .models import Asset, Customer, Contract, Personnel
# Register your models here.


# define the display of the asset table in the admin page
class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_name','asset_type','asset_assigned_personnel', 'asset_contract']


# define the display of the customer table in the admin page
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_mobile_number','customer_creation_date']


# define the display of the contract table in the admin page
class ContractAdmin(admin.ModelAdmin):
    list_display = ['contract_customer','contract_start_date','contract_end_date']


# define the display of the personnel table in the admin page
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ['personnel_name','personnel_role']


# register the models in the admin page
admin.site.register(Asset, AssetAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Personnel, PersonnelAdmin)