from django.urls import path
from .views import billing
urlpatterns = [
    path('generateInvoice',billing),
]
