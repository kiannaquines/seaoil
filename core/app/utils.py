from django.utils import timezone
import random

def receipt_number_generator():
    return f'{random.randint(100, 200)}{timezone.now().strftime("%Y%m%d")}'