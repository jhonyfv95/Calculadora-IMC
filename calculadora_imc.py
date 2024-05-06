#Esta es una calculadora de IMC en python
#Creado por: Jhonnathan Fuentes
#Creada con base en el ejemplo que se ve en el curso de python para principiantes de ucamp 2024

try:
    #Pedimos los datos de introducción del usuario
    nombre = input("Hola, por favor introduce tu(s) nombre(s): ")
    apellidoP = input("Intoduce tu apellido paterno: ")
    apellidoM = input("Intoduce tu apellido materno: ")
    edad = int(input("¿Cuantos años tienes? "))
    peso = float(input("¿Cuál es tu peso en KG? "))
    altura = float(input("¿Cuál es tu altura en Mts? "))
except:
    #Cachamos el error
    print("Ha ocurrido un error, por favor introduzca los datos correctos (recuerde que edad debe ser en años [25], peso en kilos [70] y altura en metros [1.68])")

try:
    #Calculamos el IMC
    IMC = round(peso / altura ** 2)
    print("Tu índice de masa corporal es: " + str(IMC))
    #Se imprime el IMC de acuerdo a los datos introducidos del usuario
    datos = nombre + " " + apellidoP + " " + apellidoM
    msj = " usted tiene "
    if IMC >= 0 and IMC <= 15.99 :
        print ("Hola " + datos + msj + "delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Hola " + datos + msj + "delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Hola " + datos + msj + "delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        msj = " usted se encuentra "
        print ("Hola " + datos + msj + "en su peso óptimo")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Hola " + datos + msj + "sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("Hola " + datos + msj + "obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("Hola " + datos + msj + "obesidad media")
    elif IMC >= 40.00:
        print ("Hola " + datos + msj + "obesidad morbida")
except:
    print("Ha ocurrido un error, no se ha podido calcular su IMC")