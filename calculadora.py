# Calculadora

operación = input("Ingresar operación a realizar ( +,-,*, / ):")

if operación == "+":
    num1 = float(input("Ingrese el primer valor a sumar:"))
    num2 = float(input("Ingrese segundo valor:"))
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif operación == "-":
    num1 = float(input("Ingrese el primer valor a restar:"))
    num2 = float(input("Ingrese el segundo valor:"))
    resultado = num1 - num2
    print(f"{num1}-{num2} = {resultado}")

elif operación == "*":
    num1 = float(input("Ingrese el primer valor a multiplicar:"))
    numr2 = float(input("Ingrese segundo valor a multiplicar:"))
    resultado = num1 * numr2
    print(f"{num1}*{numr2} = {resultado}")

elif operación == "/":
    num1 = float(input("Ingrese el primer valor a divir:"))
    num2 = float(input("Ingrese el segundo valor:"))
    resultado = num1 / num2
    print(f"{num1}/{num2} = {resultado}")

else:
    print("Esta calculadora no esta programada para realizar esa operación.!Vuelva pronto¡.")
