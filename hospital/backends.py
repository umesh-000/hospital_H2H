from django.contrib.auth.backends import BaseBackend
from .models import Customer

class PhoneNumberBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            print("Attempting authentication")
            customer = Customer.objects.get(phone_number=phone_number)
            print("Customer found:", customer)
            if customer.check_password(password):
                return customer
        except Customer.DoesNotExist:
            print("Customer does not exist")
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None

