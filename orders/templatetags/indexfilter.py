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
    return d[key].client.user
@register.filter
def lookupmethod(d, key):
    return d[key].paymentMethod
