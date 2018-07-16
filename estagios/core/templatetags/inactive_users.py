from django import template
from ..models import User

register = template.Library()


@register.simple_tag
def inactive_users():
    return User.objects.filter(is_active=False)
