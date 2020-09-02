""" Return quarter hour chunks in a manner that humans like """
import decimal
from django import template
register = template.Library()


@register.filter(name='hours')
def hours(value):
    """ Return in hours """
    if value:
        try:
            return value / decimal.Decimal(4)
        except TypeError:
            print(f"TypeError in hours: {hours}={type(hours)}")
            return 'E'
    return '0'
