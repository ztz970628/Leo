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


@register.filter
def get_filter(obj):
    """
    是一个查询商品上架类型的实例对象
    """
    result = obj.filter(statue=1)[:4]
    return result


@register.filter('set_phone')
def set_phone(obj):
    """
    拼接手机号使用,隐私
    """
    result = obj[:3] + '***' + obj[7:]
    return result