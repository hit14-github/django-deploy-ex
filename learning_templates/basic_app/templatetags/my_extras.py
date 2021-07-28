from django import template

register = template.Library()

#using decorators
@register.filter(name='dcut')
def dcut(value,arg):
    """
    This cuts out all values of arg fromt the string
    """
    return value.replace(arg,'')

#normal way
#register.filter('dcut', dcut)
