from django import template
from django.utils import timezone



register = template.Library()

@register.filter
def split_timesince(value):
    return value.split(',')[0]






register = template.Library()

@register.filter
def days_left(value):
    if value:
        delta = value - timezone.now().date()
        return delta.days
    return ""
