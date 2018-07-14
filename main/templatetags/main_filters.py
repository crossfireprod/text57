from django import template

from main.models import User

register = template.Library()


@register.filter(name='get_flash_id')
def get_flash_id(value):
    return '"flash-' + str(value) + '"'
