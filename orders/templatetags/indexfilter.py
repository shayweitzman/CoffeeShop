from django import template
register = template.Library()
@register.filter
def lookup(d, key):
    return d[key]
@register.filter
def lookupid(d, key):
    return d[key].id
@register.filter
def lookupusername(d, key):
    if d[key].client is None:
        return str(d[key].fullname)
    if not d[key].client is None and d[key].client.Is_VIP:
        return str(d[key].fullname) + ' VIP User'
    return d[key].fullname
@register.filter
def lookupmethod(d, key):
    return d[key].paymentMethod
