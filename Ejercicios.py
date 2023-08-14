#1. Clasificación de Calificaciones: 
# Crea un programa que solicite al usuario ingresar una calificación numérica (del 0 al 100).
# Luego, muestra un mensaje indicando la clasificación de la calificación, 
# según la siguiente escala: "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) y "F" (0-59). 


nombre = input("Ingrese su nombre: \n")
calificacion = float(input("Ingrese su calificación, en el rango del 0 al 100: \n"))

if calificacion >= 90 and calificacion <=100:
    print(nombre, "Obtuviste una 'A'\nTu calificación se encuentra posicionada en un excelete rango (90-100).")
elif calificacion >= 80 and calificacion <= 89:
    print(nombre, "Obtuviste una 'B'\nTu calificación se encuentra posicionada en un buen rango (80-89).")
elif calificacion >= 70 and calificacion <= 79:
    print(nombre, "Obtuviste una 'C'\nTu calificación se encuentra posicionada en un buen rango (70-79).")
elif calificacion >= 60 and calificacion <= 69:
    print(nombre, "Obtuviste una 'D'\nTu calificación actual se encuentra en un rango de 60-69")
elif calificacion >= 0 and calificacion <= 59:
    print(nombre, "Obtuviste una 'F'\nTu calificación actual se encuentra en un rango de 0-59")
else:
    print(nombre, "La calificación escrita no pertenece al rango estipulado.")
    


# 2. Determinar Número Mayor: 
# Desarrolla un programa que solicite al usuario ingresar tres números enteros diferentes. 
# Luego, encuentra y muestra cuál de ellos es el número mayor.    

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))

if num1 > num2 and num1 > num3:
    numMayor = num1
elif num2 > num1 and num2 > num3:
    numMayor = num2
else:
    numMayor = num3

print("El número mayor es: ", numMayor)


#3. Verificación de Contraseña: 
# Desarrolla un programa que pida al usuario ingresar una contraseña. Si la contraseña ingresada es "secreto123", 
# muestra un mensaje de "Acceso permitido"; de lo contrario, muestra un mensaje de "Acceso denegado". 

contraseña = "secreto123"
input("Ingrese la contraseña correcta: \n")
if contraseña == "secreto123":
    print("Acceso permitido.")
else:
    print("Acceso denegado.")
    

#4. Comparación de Números: 
# Escribe un programa que solicite al usuario ingresar dos números enteros diferentes. 
# Luego, compara los números y muestra un mensaje indicando cuál de ellos es el mayor o si son iguales. 


numeroUno = int(input("Ingresa un número entero: "))
numeroDos = int(input("Ingresa un número entero diferente del anterior: "))

if numeroUno > numeroDos:
    print("El número mayor es ", numeroUno)
elif numeroDos > numeroUno:
    print("El número mayor es ", numeroDos)
else:
    print("Los números ingresados son iguales.")


#5. Clasificación de Edades: 
# Escribe un programa que pida al usuario ingresar su edad. 
# Luego, clasifica la edad ingresada en una de las siguientes categorías: 
# "Niño" (0-12 años), "Adolescente" (13-19 años), 
# "Adulto Joven" (20-39 años), "Adulto" (40-59 años) o "Adulto Mayor" (60 años en adelante). 
# Muestra un mensaje con la categoría correspondiente. 
categoria1 = "Niño"
categoria2 = "Adolescente"
categoria3 = "Adulto Joven"
categoria4 = "Adulto"
categoria5 = "Adulto Mayor"

edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad <= 12:
    print("Su edad se encuentra dentro de la categoría: ", categoria1)
elif edad >= 13 and edad <= 19:
    print("Su edad se encuentra dentro de la categoría: ", categoria2)
elif edad >= 20 and edad <= 39:
    print("Su edad se encuentra dentro de la categoría: ", categoria3)
elif edad >= 40 and edad <= 59:
    print("Su edad se encuentra dentro de la categoría: ", categoria4)
else:
    print("Su edad se encuentra dentro de la categoría: ", categoria5)


#6. Clasificación de Triángulos: 
# Escribe un programa que pida al usuario ingresar tres longitudes correspondientes a los lados de un triángulo. 
# Luego, determina y muestra la clasificación del triángulo según sus lados: "Equilátero" si los tres lados son iguales, 
# "Isósceles" si dos lados son iguales, o "Escaleno" si los tres lados son diferentes. 

lado1 = input("Escriba la primer medida del triángulo: ")
lado2 = input("Escribe la segunda medida del triángulo: ")
lado3 = input("Escribe la tercer medida del triángulo: ")    
tria1 = "Triángulo Equilatero"
tria2 = "Triángulo Escaleno"
tria3 = "Triángulo Isóceles"

if lado1 == lado2 and lado1 == lado3:
    print("Clasificación del triángulo: ", tria1)
elif lado1 != lado2 and lado1 != lado3:
    print("Clasificación del triángulo: ", tria2)
else:
    print("Clasificación del triángulo: ", tria3)
    

#7. Suma de Dígitos: 
# Crea un programa que solicite al usuario ingresar un número entero positivo. 
# Utiliza un ciclo "while" para sumar todos los dígitos del número ingresado. Muestra la suma total al final. 

numInt = int(input("Digita un número entero positivo: "))
digitosSuma = 0
while numInt > 0:
    dig = numInt % 10
    digitosSuma += dig
    numInt //= 10
suma = print("La suma de los digitos es: ", digitosSuma)
    

#8. Suma de Números: 
# Crea un programa que pida al usuario ingresar números enteros positivos. 
# Utiliza un ciclo "while" para sumar los números ingresados hasta que el usuario ingrese un número negativo. 
# Muestra la suma total al final. 

total = 0
while True:
    numInt1 = int(input("Ingresa un número entero positivo: "))
    if numInt1 < 0:
        break
    total += numInt1
print("El total de la suma es de: ", total)



#9. Tabla de Multiplicar: 
# Crea un programa que solicite al usuario ingresar un número entero. 
# Utiliza un bucle "for" para imprimir la tabla de multiplicar del número ingresado, desde el 1 hasta el 10. 

numerO = int(input("Ingresa un número entero: "))

print(f"Tabla de multiplicar del: ", numerO)

for i in range(1, 11):
    toTal = numerO * i
    print(f"{numerO} x {i} = {toTal}")
 
  
#10. Números Pares en un Rango: 
# Crea un programa que solicite al usuario ingresar dos números enteros, un límite inferior y un límite superior. 
# Utiliza un bucle "for" para imprimir todos los números pares dentro del rango especificado (incluyendo los límites) 


limInferior = int(input("Ingresa el límite inferior: "))
limSuperior = int(input("Ingresa el límite superior: "))

if limInferior > limSuperior:
    print("El límite inferior debe ser menor o igual al límite superior.")
else:
    print(f"Números pares entre {limInferior} y {limSuperior}: ")

    for numero in range(limInferior, limSuperior + 1):
        if numero % 2 == 0:
            print(numero)


#11. Comprobación de Validez de Usuario: 
# Crea un programa que solicite al usuario ingresar su nombre de usuario y su edad. 
# Utiliza el operador "AND" para evaluar si el nombre de usuario no está vacío y si la edad es mayor o igual a 18 años.
# Si ambas condiciones son verdaderas, muestra un mensaje que indique que el usuario es válido. 

def user():
    nombre = input("Ingresa tu nombre de usuario: ")
    edad = int(input("Ingresa tu edad: "))
    if nombre != "" and edad >= 18:
        print("Usuario válido.")
    else:
        print("Usuario no válido.")
if __name__ == "__main__":
    user()
    

#12. Acceso al Sistema: 
# Crea un programa que solicite al usuario ingresar su nombre de usuario y contraseña. 
# Luego, verifica si el nombre de usuario es "admin" y la contraseña es "12345" utilizando el operador "AND". 
# Si ambas condiciones son verdaderas, muestra un mensaje de bienvenida al sistema. 

nomUser = input("Ingresa tu nombre de usuario: ")
contraseña = input("Ingresa tu contraseña: ")

if nomUser == "admin" and contraseña == "12345":
    print("Bienvenid@ al sistema, ", nomUser,".")
else: 
    print("Algo salió mal, verifica tu contraseña y nombre de usuario.")
    

#13. Ingreso a una Película: 
# Crea un programa que solicite al usuario su edad y si está acompañado de un adulto. 
# Utiliza el operador "OR" para verificar si la edad es mayor o igual a 18 años o si está acompañado de un adulto. 
# Si alguna de las condiciones es verdadera, permite el ingreso a la película; de lo contrario, 
# muestra un mensaje indicando que el acceso está restringido. 

edadUsuario = int(input("Ingresa tu edad: "))
acompañ = input("¿Viene acompañado por un adulto?\nSi\nNo\n")
if edadUsuario >= 18 or acompañ == "si".lower:
    print("Acceso permitido.\nDisfrute de la película.")
else: 
    print("Acceso restringido.")
    

#14. Concesión de Préstamo: 
# Escribe un programa que solicite al usuario ingresar su salario anual y el número de años de empleo actual. 
# Utiliza el operador "OR" para verificar si el salario es mayor a $30,000 o si ha trabajado en la empresa 
# por al menos 2 años. Si alguna de las condiciones es verdadera, muestra un mensaje aprobando el préstamo; 
# de lo contrario, muestra un mensaje indicando que el préstamo no ha sido aprobado. 

salarioAnual = float(input("Ingrese la cantidad de su salario anual: "))
añosEmpleo = int(input("Ingresa la cantidad de años que llevas laborando actualmente: "))
if salarioAnual > 30000 or añosEmpleo >= 2:
    print("¡Su préstamo ha sido aprobado!")
else:
    print("Su préstamo ha sido rechazado.")



#15. Acceso a una Función: 
# Escribe una función que reciba un parámetro booleano que indica si un usuario ha iniciado sesión. 
# Utiliza el operador "NOT" para verificar si el usuario no ha iniciado sesión. Si el usuario no ha iniciado sesión, 
# muestra un mensaje que indique que debe iniciar sesión para acceder a la función. 

def inicioSesion(usuarioInicio):
    if not usuarioInicio:
        print("Inicia sesión para acceder a la función.")
    else:
        print("Acceso permitido.")
usuarioInicioSesion = False # o True
inicioSesion(usuarioInicioSesion)
 

#16. Verificación de Edad: 
# Crea un programa que solicite al usuario ingresar su edad. 
# Utiliza el operador "NOT" para verificar si el usuario es menor de edad (es decir, tiene menos de 18 años). 
# Si el usuario es menor de edad, muestra un mensaje que indique que debe ser mayor de edad para acceder 
# a cierta funcionalidad.

def main():
    edadUser = int(input("Ingrese su edad: "))
    if not mayorDeEdad(edadUser):
        print("Debe ser mayor de edad para acceder a esta función.")
    else:
        print("Acceso permitido.")
def mayorDeEdad(edad):
    return edad >= 18
if __name__ == "__main__":
    main()

    
