from django import template
import numpy

register = template.Library()

# =============================================================================
# Start of matrix custom tags
# =============================================================================
@register.simple_tag
def matrix_2D(a1,b1,d1,a2,b2,d2):
# Check if form has been populated yet
    if a1==a2==b1==b2==d1==d2=='':
        return 'N/A'
# If form is populated, solve the system
    else:
        a1 = float(a1)
        b1 = float(b1)
        d1 = float(d1)
        a2 = float(a2)
        b2 = float(b2)
        d2 = float(d2)
    # construct matrix 
        matrix = numpy.array([[a1,b1],[a2,b2]])
        constants = numpy.array([[d1],[d2]])
    # check for singular matrix possibilities
        if numpy.linalg.det(matrix) == 0 and a1 == 0 and b1 == 0:
            return 'Infinte Solutions'
        elif numpy.linalg.det(matrix) == 0 and a2/a1 == b2/b1 and d1 == d2 == 0:
            return 'Infinite Solutions'
        elif numpy.linalg.det(matrix) == 0 and a2/a1 == b2/b1 == d2/d1:
            return 'Infinite Solutions'
        elif numpy.linalg.det(matrix) == 0 and a2/a1 == b2/b1 != d2/d1:
            return 'No Solutions'
    # if matrix is not singular
        else:
            try:
                s = numpy.linalg.solve(matrix,constants)
                validate = True
            except:
                validate = False
            
            if validate == True:
                return '({},{})'.format(numpy.around(s[0][0],decimals=1),numpy.around(s[1][0],decimals=1))
            else:
                return 'Invalid Input'