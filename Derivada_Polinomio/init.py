"""
@autor: Mario Alberto Florentino Miguel
@github: https://github.com/Mithrandirflormig
@correo: yondaimeflormig@ciencias.unam.mx
"""
from Separate_Terms import Separate_terms
from Separate_Coeficients import Separate_coeficients
from Product_Coeficients import Product_coeficients
from Constructing_Derivative import Constructing_derivative

'''En este script encontraremos dos posibilidades para ejecutar el programa:
1. Una función que devuelve únicamente la derivada correspondiente
2. Una función que aplica recursividad para devolver todas las derivadas hasta llegar a 0'''

print("El siguiente programa calcula la derivada de un polinomio de la forma p(x) = a0x^0 + a1x^1 + a2x^2 + a3x^3 + ... + anx^n")

#Forma 1. Devolución de la derivada correspondiente
def init(expression):
    separate_terms = Separate_terms(expression)
    coeficients, exponents = Separate_coeficients(separate_terms)
    new_coeficients, new_exponents = Product_coeficients(coeficients, exponents)
    derivative = Constructing_derivative(new_coeficients, new_exponents)

    return derivative 

#En caso de realizar pruebas comentar las siguiente líneas
polynomial = input("Ingresa el polinomio f(x) = ")
result = init(polynomial)
print(f"f¹(x) = {result}")


'''
#Forma 2. Encontrando todas las derivadas posibles mediante recursividad
def init(expression):
    #Basecase
    if 'x' not in expression:
        expr.append('0')
    else:
        separate_terms = Separate_terms(expression)
        coeficients, exponents = Separate_coeficients(separate_terms)
        new_coeficients, new_exponents = Product_coeficients(coeficients, exponents)
        derivative = Constructing_derivative(new_coeficients, new_exponents)
        expr.append(derivative)
        init(derivative)

expr = []
cont = 0
format_index = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]

polynomial = input("Ingresa el polinomio f(x) = ")
init(polynomial)

while cont <= 8:
    try:
        print(f"f{format_index[cont+1]}(x) = {expr[cont]}")
        cont += 1
    except IndexError:
        break
else:
    more_index = [f"{format_index[i]}{format_index[j]}" for i in range(1,len(format_index)) for j in range(len(format_index))]
    for i in range(len(expr)-cont):
        print(f"f{more_index[i]}(x) = {expr[cont+i]}")
'''