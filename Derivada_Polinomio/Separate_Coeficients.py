"""
@autor: Mario Alberto Florentino Miguel
@github: https://github.com/Mithrandirflormig
@correo: yondaimeflormig@ciencias.unam.mx
"""
def Separate_coeficients(list_terms):
    coeficients = [] 
    exponents = [] 
    coef_term = '' 

    if '-' not in list_terms[0] and list_terms[0][0] == 'x':
        coef_term = "+"

    for term in list_terms:
        if ('x' not in term and '^' not in term) or ('x' not in term and '^' in term): 
            continue
        elif 'x' in term and '^' not in term:
            coeficients.append(term[:-1])
            exponents.append('1')
        else:
            for caracter in term: 
                if caracter == 'x':
                    coeficients.append(coef_term)
                    coef_term = '' 
                    continue
                elif caracter == '^':
                    continue
                coef_term += caracter 

            exponents.append(coef_term)
            coef_term = ''

    return coeficients, exponents