"""
@autor: Mario Alberto Florentino Miguel
@github: https://github.com/Mithrandirflormig
@correo: yondaimeflormig@ciencias.unam.mx
"""
def Separate_terms(expression):
    sum_term = ''
    separate_terms = []

    for caracter in expression:
        if caracter == '+' or caracter == '-':
            separate_terms.append(sum_term)
            sum_term = ''
        elif caracter == ' ':
            continue 
        sum_term += caracter
    separate_terms.append(sum_term)

    if '' in separate_terms:
        separate_terms.pop(0)

    return separate_terms