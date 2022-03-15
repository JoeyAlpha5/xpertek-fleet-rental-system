from django.db import models
from datetime import date

# Create your models here.

qualification_options = [("Diploma","Diploma"), ("Degree", "Degree")]
personnel_roles = [("Forklift Operator", "Forklift Operator"), ("Driver", "Driver")]
asset_type = [("Forklift", "Forklift"), ("Vehicle", "Vehicle")]

# customer model
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200,blank=False,null=False)
    customer_mobile_number = models.CharField(max_length=200,blank=False,null=False)
    customer_email_address = models.CharField(max_length=200,blank=False,null=False)
    customer_creation_date = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    customer_update_date = models.DateTimeField(auto_now=True,blank=False,null=False)

    def __str__(self):
        return self.customer_name

    # order the customer list by customer id
    class Meta:
        ordering = ['-id']


class Personnel(models.Model):
    id = models.AutoField(primary_key=True)
    personnel_id_number = models.CharField(max_length=200,blank=False,null=False)
    personnel_name = models.CharField(max_length=200,blank=False,null=False)
    personnel_daily_rate = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
    personnel_qualification = models.CharField(max_length=200, choices=qualification_options,blank=False,null=False)
    personnel_role = models.CharField(max_length=200, choices=personnel_roles,blank=False,null=False)
    personnel_creation_date = models.DateTimeField(auto_now_add=True)
    personnel_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.personnel_name

    # order the personnel list by personnel id
    class Meta:
        ordering = ['-id']
        


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    contract_customer = models.OneToOneField(Customer, on_delete=models.CASCADE,blank=False,null=False)
    contract_start_date = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    contract_end_date = models.DateField(blank=False,null=False)
    contract_last_update_date = models.DateTimeField(auto_now=True)
    contract_max_km_per_trip = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
    contract_overage_charge = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)

    def __str__(self):
        return self.contract_customer.customer_name

    # order the contract list by contract id
    class Meta:
        ordering = ['-id']


class Asset(models.Model):
    id = models.AutoField(primary_key=True)
    asset_tracker_id = models.CharField(max_length=200,blank=False,null=False)
    asset_name = models.CharField(max_length=200,blank=False,null=False)
    asset_type = models.CharField(max_length=200, choices=asset_type,blank=False,null=False)
    asset_model = models.CharField(max_length=200,blank=False,null=False)
    asset_registration_number = models.CharField(max_length=200,blank=False,null=False)
    asset_daily_selling_price = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False)
    asset_assigned_personnel = models.OneToOneField(Personnel, on_delete=models.CASCADE,blank=False,null=False)
    asset_contract = models.ForeignKey(Contract, on_delete=models.CASCADE,blank=False,null=False)


    def __str__(self):
        return self.asset_name

    # order the asset list by asset id
    class Meta:
        ordering = ['-id']