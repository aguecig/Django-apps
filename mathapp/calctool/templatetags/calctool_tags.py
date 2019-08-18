from django import template
import sympy
from sympy import init_printing, latex
# init pretty printing
init_printing()

register = template.Library()

#from ..models import Function


# =============================================================================
# Start of calculus custom tags

# Each tag goes through the following:

# (1) Handle user syntax so it is acceptable for sympy
#       - eg  if user inputs x^2 this is changed to x**2
# (2) Handle any exceptions for invalid input
# (3) If input is valid, run the function, and output result in latex format
#     which can then be passed into the HTML template for pretty printing
# (4) If input is not valid, return a message in the HTML template stating this
# =============================================================================
x = sympy.symbols('x')

# take the user function input and convert to latex style
@register.simple_tag
def latex_function(function):
# handle user syntax 
    function = function.replace('^','**')
    for char in [chr(i) for i in range(48,58)]:
        function = function.replace('{}x'.format(char),'{}*x'.format(char))
        for f in ['sqrt','exp','ln','log','sin','cos','tan','sec','csc','cot','(']:
            function = function.replace('{}{}'.format(char,f),'{}*{}'.format(char,f))
            function = function.replace('x{}'.format(f),'x*{}'.format(f))
            function = function.replace('){}'.format(f),')*{}'.format(f))
# check for invalid input        
    try:
        latex(sympy.simplify(function))
        validate = True
    except:
        validate = False
        
    if validate == True:
        return latex(sympy.simplify(function))
    else:
        return 'Invalid-Input'
    
# find limit of a function at a point
@register.simple_tag
def limit(function,point):
# handle user syntax 
    function = function.replace('^','**')
    for char in [chr(i) for i in range(48,58)]:
        function = function.replace('{}x'.format(char),'{}*x'.format(char))
        for f in ['sqrt','exp','ln','log','sin','cos','tan','sec','csc','cot','(']:
            function = function.replace('{}{}'.format(char,f),'{}*{}'.format(char,f))
            function = function.replace('x{}'.format(f),'x*{}'.format(f))
            function = function.replace('){}'.format(f),')*{}'.format(f))
# check for invalid input            
    try:
        sympy.limit(function,x,point)
        validate = True
    except:
        validate = False
        
    if validate == True:
        return latex(sympy.limit(function,x,point)) 
    else:
        return 'N/A'

# find first derivative of user function input
@register.simple_tag
def derivative(function):
# handle user syntax 
    function = function.replace('^','**')
    for char in [chr(i) for i in range(48,58)]:
        function = function.replace('{}x'.format(char),'{}*x'.format(char))
        for f in ['sqrt','exp','ln','log','sin','cos','tan','sec','csc','cot','(']:
            function = function.replace('{}{}'.format(char,f),'{}*{}'.format(char,f))
            function = function.replace('x{}'.format(f),'x*{}'.format(f))
            function = function.replace('){}'.format(f),')*{}'.format(f))
# check for invalid input            
    try:
        sympy.diff(function,x)
        validate = True
    except:
        validate = False
        
    if validate == True:
        return(latex(sympy.diff(function,x)))
    else:
        return 'Invalid-Input'
 
# find integral of user function input if possible
@register.simple_tag
def integral(function):
    # handle user syntax 
    function = function.replace('^','**')
    for char in [chr(i) for i in range(48,58)]:
        function = function.replace('{}x'.format(char),'{}*x'.format(char))
        for f in ['sqrt','exp','ln','log','sin','cos','tan','sec','csc','cot','(']:
            function = function.replace('{}{}'.format(char,f),'{}*{}'.format(char,f))
            function = function.replace('x{}'.format(f),'x*{}'.format(f))
            function = function.replace('){}'.format(f),')*{}'.format(f))

# check for invalid input            
    try:
        sympy.integrate(function,x)
        validate = True
    except:
        validate = False
        
    if validate == True:
        return(latex(sympy.integrate(function,x)))
    else:
        return 'Invalid-Input'

# find critical points of user function input    
@register.simple_tag
def critpoints(function):
# handle user syntax 
    function = function.replace('^','**')
    for char in [chr(i) for i in range(48,58)]:
        function = function.replace('{}x'.format(char),'{}*x'.format(char))
        for f in ['sqrt','exp','ln','log','sin','cos','tan','sec','csc','cot','(']:
            function = function.replace('{}{}'.format(char,f),'{}*{}'.format(char,f))
            function = function.replace('x{}'.format(f),'x*{}'.format(f))
            function = function.replace('){}'.format(f),')*{}'.format(f))
# check for invalid input    
    try:
        sympy.diff(function,x)
        fprime = sympy.diff(function,x)
        cpoints = sympy.solveset(fprime,x,domain=sympy.S.Reals)
        validate = True
    except:
        validate = False
        
    if validate == True:

        fprime = sympy.diff(function,x)
        cpoints = sympy.solveset(fprime,x,domain=sympy.S.Reals)
        
        # Handle special errors
        
# check for infinite solutions
        if type(cpoints) == sympy.Union:
            return 'Infinite-Solutions'
# condition set error, found when i used something like function = xexp(x) lack of *
        elif type(cpoints) == sympy.ConditionSet:
            return 'N/A'
# complement error when i used something like 4xlog(1-x)
        elif type(cpoints) == sympy.Complement:
            return 'N/A'
# check if all real numbers are critical points        
        elif cpoints == sympy.Reals:
            return 'All-of-R'

        
        else:
            # check if no solutions exist
            if len(cpoints) == 0:
                return 'None'
            else:
                points = ''
                for point in cpoints:
                    points += 'x = {} \quad '.format(latex(sympy.simplify(point)))
                return points
    else:
        return 'Invalid-Input'

# find inflection points of user function input
@register.simple_tag
def infpoints(function):
# handle user syntax 
    function = function.replace('^','**')
    for char in [chr(i) for i in range(48,58)]:
        function = function.replace('{}x'.format(char),'{}*x'.format(char))
        for f in ['sqrt','exp','ln','log','sin','cos','tan','sec','csc','cot','(']:
            function = function.replace('{}{}'.format(char,f),'{}*{}'.format(char,f))
            function = function.replace('x{}'.format(f),'x*{}'.format(f))
            function = function.replace('){}'.format(f),')*{}'.format(f))        
# check for invalid input    
    try:
        sympy.diff(function,x)
        ftwoprime = sympy.diff(function,x,x)
        ipoints = sympy.solveset(ftwoprime,x,domain=sympy.S.Reals)
        validate = True
    except:
        validate = False
        
    if validate == True:
        
        ftwoprime = sympy.diff(function,x,x)
        ipoints = sympy.solveset(ftwoprime,x,domain=sympy.S.Reals)
        
        # Handle special errors
        
# check for infinite solutions        
        if type(ipoints) == sympy.Union:
            return 'Infinite-Solutions'
# condition set error
        elif type(ipoints) == sympy.ConditionSet:
            return 'N/A'
# complement error 
        elif type(ipoints) == sympy.Complement:
            return 'N/A'
# check if all real numbers are critical points            
        elif ipoints == sympy.Reals:
            return 'All-of-R'
        
        
        else:
            # check if no solutions exist
            if len(ipoints) == 0:
                return 'None'
            else:
                points = ''
                for point in ipoints:
                    points += 'x = {} \quad '.format(latex(sympy.simplify(point)))
                return points
    else:
        return 'Invalid-Input'
    
# =============================================================================
# End of calculus custom tags
# =============================================================================