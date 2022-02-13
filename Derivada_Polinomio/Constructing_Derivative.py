"""
@autor: Mario Alberto Florentino Miguel
@github: https://github.com/Mithrandirflormig
@correo: yondaimeflormig@ciencias.unam.mx
"""
def Constructing_derivative(new_coeficients, new_exponents):
    expression = ''

    for position in range(len(new_coeficients)):
        if float(new_coeficients[position]) == 0:
            continue
        elif int(new_exponents[position]) == 0:
            if '-' not in new_coeficients[position]:
                expression += '+' + new_coeficients[position]
            else:
                expression += new_coeficients[position]
        elif int(new_exponents[position]) == 1:
            if '-' not in new_coeficients[position]:
                expression += '+' + new_coeficients[position] + 'x'
            else:
                expression += new_coeficients[position] + 'x'
        else:
            if '-' not in new_coeficients[position]:
                expression += '+' + new_coeficients[position] + 'x^' + new_exponents[position]
            else:
                expression += new_coeficients[position] + 'x^' + new_exponents[position] 

    if expression == '':
        expression = '0'

    return expression