from django import template

register = template.Library()

# =============================================================================
# Check answers for alkanes, alkenes, alkynes, alcohols and cyclo alkanes
# =============================================================================
@register.simple_tag
def question1(q1): 
    if q1 == '':
       return ''
    
    elif q1 == '2,2-diethylbutan-1,3-diol':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question2(q2):
    if q2 == '':
       return ''
    
    elif q2 == '2,3,6-trimethyloctane':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question3(q3):
    if q3 == '':
       return ''
    
    elif q3 == '2-methylbut-1,3-diene':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question4(q4):
    if q4 == '':
       return ''
    
    elif q4 == '2-methylcyclobutene':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question5(q5):
    if q5 == '':
       return ''
    
    elif q5 == '2-methylhex-3-ene':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question6(q6):
    if q6 == '':
       return ''
    
    elif q6 == '2-propylpentan-1-ol':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question7(q7):
    if q7 == '':
       return ''
    
    elif q7 == '5-ethyl-3-methylheptan-2-ol':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question8(q8):
    if q8 == '':
       return ''
    
    elif q8 == 'methylcyclohexane':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question9(q9):
    if q9 == '':
       return ''
    
    elif q9 == 'pent-1,3-diyne':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question10(q10):
    if q10 == '':
       return ''
    
    elif q10 == 'propene':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question11(q11):
    if q11 == '':
       return ''
    
    elif q11 == '3-methylpentanal':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question12(q12):
    if q12 == '':
       return ''
    
    elif q12 == '4,5-dimethylnonan-3-one':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question13(q13):
    if q13 == '':
       return ''
    
    elif q13 == '1-ethoxypropane':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question14(q14):
    if q14 == '':
       return ''
    
    elif q14 == '4-methylhexan-3-one':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question15(q15):
    if q15 == '':
       return ''
    
    elif q15 == '2-ethylbutanal':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question16(q16):
    if q16 == '':
       return ''
    
    elif q16 == '2-ethoxybutane':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question17(q17):
    if q17 == '':
       return ''
    
    elif q17 == '4-methylpentan-2-one':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question18(q18):
    if q18 == '':
       return ''
    
    elif q18 == 'cyclohexanal':
        return 'Correct!'
    else:
        return 'Incorrect :( '
        
@register.simple_tag
def question19(q19):
    if q19 == '':
       return ''
    
    elif q19 == 'methylpropanone':
        return 'Correct!'
    else:
        return 'Incorrect :( '
    

#        
#    if q3 == 
#        answers[2] = 'Correct'
#    else:
#        answers[2] = 'Incorrect'
#        
#    if q4 == 
#        answers[3] = 'Correct'
#    else:
#        answers[3] = 'Incorrect'
#        
#    if q5 == 
#        answers[4] = 'Correct'
#    else:
#        answers[4] = 'Incorrect'
#        
#    if q6 == 
#        answers[5] = 'Correct'
#    else:
#        answers[5] = 'Incorrect'
#        
#    if q7 == 
#        answers[6] = 'Correct'
#    else:
#        answers[6] = 'Incorrect'
#        
#    if q8 == 
#        answers[7] = 'Correct'
#    else:
#        answers[7] = 'Incorrect'
#        
#    if q9 == 
#        answers[8] = 'Correct'
#    else:
#        answers[8] = 'Incorrect'
#        
#    if q10 == 
#        answers[9] = 'Correct'
#    else:
#        answers[9] = 'Incorrect'
#        
#    correct = []
#    incorrect = []
#
#    
#    for i in range(10):
#        if answers[i] == 'Correct':
#            correct.append(i+1)
#        elif answers[i] == 'Incorrect':
#            incorrect.append(i+1)
#            
#    return 'Correct answers were given to the following questions so far: {}'.format(correct)
#        