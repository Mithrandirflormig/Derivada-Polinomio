"""
@autor: Mario Alberto Florentino Miguel
@github: https://github.com/Mithrandirflormig
@correo: yondaimeflormig@ciencias.unam.mx
"""
from math import sqrt, sin, cos, tan, log, exp #Algunas funciones típicas que podrían aparecer

#Forma 1. Usando la función eval
def Product_coeficients(coeficients, exponents):
    new_coeficients = [] 
    new_exponents = [] 

    for position in range(len(coeficients)):
        if len(coeficients[position]) == 1 and coeficients[position] in ["+", "-"]: 
            num = round(eval(coeficients[position] + "1" + "*" + exponents[position]),1)
            new_coeficients.append(str(num)) 
        else:
            try:
                num = round(eval(coeficients[position] + "*" + exponents[position]),1) 
                new_coeficients.append(str(num))
            except Exception as e:
                print(f"No se puede operar el término {coeficients[position]} * {exponents[position]}")

        new_exponents.append(str(int(exponents[position])-1))

    return new_coeficients, new_exponents

#Forma 2. Sin usar la función eval
'''
def Product_coeficients(coeficients, exponents):
    new_coeficients = [] 
    new_exponents = [] 

    #Dado que ambas listas recibidas tienen la misma longitud, podemos itererar el tamaño de cualquiera
    for position in range(len(coeficients)):
        if len(coeficients[position]) == 1 and coeficients[position] in ["+", "-"]: 
            n_coeficiente = coeficients[position] + "1"
            n_coeficiente = int(n_coeficiente) * int(exponents[position])
            new_coeficients.append(str(n_coeficiente))
        else:
            n_coeficiente = coeficients[position]
            if '.' in n_coeficiente:
                n_coeficiente = float(n_coeficiente) * int(exponents[position])
                new_coeficients.append(n_coeficiente)
            else:
                n_coeficiente = int(n_coeficiente) * int(exponents[position])
                new_coeficients.append(n_coeficiente)

        new_exponents.append(int(exponents[position])-1)


    return new_coeficients, new_exponents
'''