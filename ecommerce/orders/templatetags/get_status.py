from django import template 

register = template.Library()

@register.simple_tag(name='get_status')
def get_status(status) :
    status_array = {
        0: 'CART_STAGE',
        1: 'ORDER_CONFIRMED',
        2: 'ORDER_PROCESSED',
        3: 'ORDER_DELIVERED',
        4: 'ORDER_REJECTED'
    }
    return status_array.get(status, 'UNKNOWN')
