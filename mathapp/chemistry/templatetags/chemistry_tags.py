from django import template

register = template.Library()

# =============================================================================
# Check answers for alkanes, alkenes, alkynes, alcohols and cyclo alkanes
# =============================================================================
@register.simple_tag
def section1(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10):
    answers = ['']*10
    
    if q1 == '2-2-diethylbutan-1-3-diol':
        answers[0] = 'Correct'
    else:
        answers[0] = 'Incorrect'
    
    if q2 == '2-3-6-trimethyloctane':
        answers[1] = 'Correct'
    else:
        answers[1] = 'Incorrect'
        
    if q3 == '2-methylbutan-1-3-diene':
        answers[2] = 'Correct'
    else:
        answers[2] = 'Incorrect'
        
    if q4 == '2-methylcyclobutene':
        answers[3] = 'Correct'
    else:
        answers[3] = 'Incorrect'
        
    if q5 == '2-methylhex-3-ene':
        answers[4] = 'Correct'
    else:
        answers[4] = 'Incorrect'
        
    if q6 == '2-propylpentan-1-ol':
        answers[5] = 'Correct'
    else:
        answers[5] = 'Incorrect'
        
    if q7 == '5-ethyl-3-methylheptan-2-ol':
        answers[6] = 'Correct'
    else:
        answers[6] = 'Incorrect'
        
    if q8 == 'methylcyclohexane':
        answers[7] = 'Correct'
    else:
        answers[7] = 'Incorrect'
        
    if q9 == 'pent-1-3-diyne':
        answers[8] = 'Correct'
    else:
        answers[8] = 'Incorrect'
        
    if q10 == 'propene':
        answers[9] = 'Correct'
    else:
        answers[9] = 'Incorrect'
        
    correct = []
    incorrect = []

    
    for i in range(10):
        if answers[i] == 'Correct':
            correct.append(i+1)
        elif answers[i] == 'Incorrect':
            incorrect.append(i+1)
            
    return 'Correct Questions: {},  Incorrect Questions: {}'.format(correct,incorrect)
        