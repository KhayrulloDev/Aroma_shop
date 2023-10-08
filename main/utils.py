from .models import Korzinka
from django.db.models import Q


def increment_count(id, user):
    try:
        shopping_cart = Korzinka.objects.get(Q(product_id=id) & Q(user=user))
        shopping_cart.count += 1
        shopping_cart.save()
    except:
        return False
    return True


def decrement_count(id, user):
    try:
        shopping_cart = Korzinka.objects.get(Q(product_id=id) & Q(user=user))
        shopping_cart.count -= 1
        shopping_cart.save()
    except:
        return False
    return True
