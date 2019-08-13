from django import template
import sympy
from sympy import init_printing, latex
# init pretty printing
init_printing()

register = template.Library()

from ..models import Function

x = sympy.symbols('x')

# When we construct these custom tags for our templates, we have to be 
# vigilant for the types of errors we might encounter that the default 
# Django forms would otherwise not pick up

# take the user function input and convert to latex style
@register.simple_tag
def latex_function(function):
    try:
        latex(sympy.integrate(sympy.diff(function)))
        validate = True
    except:
        validate = False
        
    if validate == True:
        return latex(sympy.integrate(sympy.diff(function)))
    else:
        return 'Invalid Input'

# find first derivative of user function input
@register.simple_tag
def derivative(function):
    try:
        sympy.diff(function,x)
        validate = True
    except:
        validate = False
        
    if validate == True:
        return(latex(sympy.diff(function,x)))
    else:
        return 'Invalid Input'
 
# find integral of user function input if possible
@register.simple_tag
def integral(function):
    try:
        sympy.integrate(function,x)
        validate = True
    except:
        validate = False
        
    if validate == True:
        return(latex(sympy.integrate(function,x)))
    else:
        return 'Invalid Input'

# find critical points of user function input    
@register.simple_tag
def critpoints(function):
# check for valid function input
    try:
        sympy.integrate(function,x)
        validate = True
    except:
        validate = False
        
    if validate == True:
        fprime = sympy.diff(function,x)
        cpoints = sympy.solveset(fprime,x,domain=sympy.S.Reals)
        
        # Handle special errors
        
# check for infinite solutions
        if type(cpoints) == sympy.Union:
            return 'Infinite Solutions'
# condition set error, found when i used something like function = xexp(x) lack of *
        elif type(cpoints) == sympy.ConditionSet:
            return 'Input Error'
# check if all real numbers are critical points        
        elif cpoints == sympy.Reals:
            return 'All of R'
        
        else:
            # check if no solutions exist
            if len(cpoints) == 0:
                return 'None'
            else:
                points = ''
                for point in cpoints:
                    points += 'x = {} '.format(point)
                return points
    else:
        return 'Invalid Input'

# find inflection points of user function input
@register.simple_tag
def infpoints(function):
# check for valid function input
    try:
        sympy.integrate(function,x)
        validate = True
    except:
        validate = False
        
    if validate == True:
        f2prime = sympy.diff(function,x,x)
        ipoints = sympy.solveset(f2prime,x,domain=sympy.S.Reals)
        
        # Handle special errors
        
# check for infinite solutions        
        if type(ipoints) == sympy.Union:
            return 'Infinite Solutions'
# condition set error
        elif type(ipoints) == sympy.ConditionSet:
            return 'Input Error'
# check if all real numbers are critical points            
        elif ipoints == sympy.Reals:
            return 'All of R'
        
        
        else:
            # check if no solutions exist
            if len(ipoints) == 0:
                return 'None'
            else:
                points = ''
                for point in ipoints:
                    points += 'x = {} '.format(point)
                return points
    else:
        return 'Invalid Input'