from django import template

register = template.Library()


@register.filter
def uper(obj):
    """
    obj是被过滤的对象
    """
    return obj.upper()  # 过滤的结果


@register.filter
def get_four(obj):
    return obj[:4]