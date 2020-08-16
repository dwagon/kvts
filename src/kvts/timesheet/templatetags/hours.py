""" Return quarter hour chunks in a manner that humans like """
import decimal
from django import template
register = template.Library()


@register.filter(name='hours')
def hours(value):
    """ Return in hours """
    return value / decimal.Decimal(4)
