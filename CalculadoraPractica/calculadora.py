

def sumar(a,b):
    return a +b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b !=0:
        return a / b
    else:
        return 'Error, división por cero'

if __name__ == "__main__":

    print("Bienvenido a la calculadora de Python")

    while True:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("\n==== Calculadora ====")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = input("Seleccione una opcion:")


        if opcion == "1":
            print("El resultado es:", sumar(a, b))
        elif opcion == "2":
            print("El resultado es:", restar(a, b))
        elif opcion == "3":
            print("El resultado es:", multiplicar(a, b))
        elif opcion == "4":
            print("El resultado es:", dividir(a, b))
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
