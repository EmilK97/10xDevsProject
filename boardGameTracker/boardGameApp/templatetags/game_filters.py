from django import template
from django.utils import timezone
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def split(value, arg):
    """
    Split a string by the given separator and return a list.
    Usage: {{ value|split:" " }}
    """
    return value.split(arg)

@register.filter
def time_since_pl(value):
    """
    Returns a string representing time difference in Polish.
    """
    if not isinstance(value, datetime):
        return ''

    now = timezone.now()
    diff = now - value
    days = diff.days

    if days == 0:
        return 'dzisiaj'
    elif days == 1:
        return '1 dzień'
    elif days < 7:
        return f'{days} dni'
    elif days < 30:
        weeks = days // 7
        if weeks == 1:
            return '1 tydzień'
        elif weeks < 5:
            return f'{weeks} tygodnie'
        else:
            return f'{weeks} tygodni'
    elif days < 365:
        months = days // 30
        if months == 1:
            return '1 miesiąc'
        elif months < 5:
            return f'{months} miesiące'
        else:
            return f'{months} miesięcy'
    else:
        years = days // 365
        if years == 1:
            return '1 rok'
        elif years < 5:
            return f'{years} lata'
        else:
            return f'{years} lat' 