from django import template
import numpy
import math
register = template.Library()

# =============================================================================
# start of quadratics custom tags 
# =============================================================================


# find the x-intercepts, if they exist
@register.simple_tag
def roots(a,b,c):
    if type(a) and type(b) and type(c) == str:
        return ''
    else:
        a = float(a)
        b = float(b)
        c = float(c)
        
    dscr = b**2-4*a*c
    
    if a == 0:
        return 'a = 0, this is not a quadratic function!'

    elif dscr < 0:
        return 'No real x-intercepts'
    
    elif dscr == 0:
        xint = -1*b/(2*a)
        return 'Exactly one x-intercept: {}'.format(numpy.around(xint,5))
    
    elif dscr > 0:
        xint1 = (-1*b + math.sqrt(dscr))/(2*a)
        xint2 = (-1*b - math.sqrt(dscr))/(2*a)
        return 'Exactly two x-intercepts: {} and {}'.format(numpy.around(xint1,5), numpy.around(xint2,5))
    

# find the location of the vertex (this always exists)
@register.simple_tag
def vertex(a,b,c):
    if type(a) and type(b) and type(c) == str:
        return ''
    else:
        a = float(a)
        b = float(b)
        c = float(c)
    
    if a == 0:
        return ''
    else:
        xcord = -1*b/(2*a)
        ycord = a*(xcord)**2 + b*(xcord) + c
        return 'Vertex located at: ({}, {})'.format(numpy.around(xcord,5), numpy.around(ycord,5))
    
# find the location of axis of symmetry
@register.simple_tag
def aos(a,b,c):
    if type(a) and type(b) and type(c) == str:
        return ''
    else:
        a = float(a)
        b = float(b)
        c = float(c)
    
    if a == 0:
        return ''
    else:
        aos = -1*b/(2*a)
        return 'Axis of symmetry: x = {}'.format(numpy.around(aos,5))
    
# find the value of the max/min of the function
@register.simple_tag
def optimum(a,b,c):
    if type(a) and type(b) and type(c) == str:
        return ''
    else:
        a = float(a)
        b = float(b)
        c = float(c)
    
    if a == 0:
        return ''
    else:
        x = -1*b/(2*a)
        opt = a*(x)**2 + b*(x) + c
        if a < 0:
            return 'Maximum value of {}'.format(numpy.around(opt,5))
        elif a > 0:
            return 'Minimum value of {}'.format(numpy.around(opt,5))