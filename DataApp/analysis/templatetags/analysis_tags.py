from django import template
import sympy

register = template.Library()

from ..models import Function

x = sympy.symbols('x')

# When we construct these custom tags for our templates, we have to be 
# vigilant for the types of errors we might encounter that the default 
# Django forms would otherwise not pick up

@register.simple_tag
def derivative(function):
    try:
        sympy.diff(function,x)
        validate = True
    except sympy.SympifyError:
        validate = False
        
    if validate == True:
        return(sympy.diff(function,x))
    else:
        return 'Invalid Input'
    
@register.simple_tag
def integral(function):
    try:
        sympy.integrate(function,x)
        validate = True
    except sympy.SympifyError:
        validate = False
        
    if validate == True:
        return(sympy.integrate(function,x))
    else:
        return 'Invalid Input'