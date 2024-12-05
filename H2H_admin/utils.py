import random

def generate_unique_code():
    prefix = 'Dr'
    unique_number = f"{random.randint(1, 99999):05d}"
    return f"{prefix}{unique_number}"