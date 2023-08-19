#1° A partir de una función dada calcular su derivada por metodo directo
#2° Luego  utilizar la formula para calcular la derivada en dos puntos f'(x)=(f(x+h)-f(x-h))/2*h
#3° Luego utilizar la formula para calcular la derivada en 4 puntos f'(x)=(f(x-2h)-8*f(x-h)+8*f(x+h)-f(x+2h))/12*h
## para funciones exponenciales utlizar exp ejemplo: exp (x)/(1+exp (2*x))-->e^x/1+e^2x
import sympy as sp

class DiferenciasCentradas:
    def diferencia_centrada_2_puntos(self, funcion, h, x):
        return (funcion.subs('x', x + h) - funcion.subs('x', x - h)) / (2 * h)
    
    def diferencia_centrada_4_puntos(self, funcion, h, x):
        return (funcion.subs('x', x - 2*h) - 8*funcion.subs('x', x - h) + 8*funcion.subs('x', x + h) - funcion.subs('x', x + 2*h)) / (12 * h)
        ##con subs sustituimos a la funcion por las operaciones establecidas por 'x' y 'h'
def main():

    funcion_expresion = input("Ingresa la función a evaluar: ")
    funcion = sp.sympify(funcion_expresion)
    
    h = float(input("Ingresa el valor de h: "))
    x = float(input("Ingresa el valor de x: "))
    
    diferencias = DiferenciasCentradas()
    
    print("Elige una opción:")
    print("1. Diferencia centrada en 2 puntos")
    print("2. Diferencia centrada en 4 puntos")
    opcion = int(input())
    
    
    if opcion == 1:
        resultado = diferencias.diferencia_centrada_2_puntos(funcion, h, x)
    elif opcion == 2:
        resultado = diferencias.diferencia_centrada_4_puntos(funcion, h, x)
    else:
        print("Opción no válida")
        return
    
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()






