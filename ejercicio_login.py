# Realizar un login. DuocUc a contratado sus servicios para realizar un login en Python. Este login debe validar el usuario y la clave con lo que han aprendido hoy en clase. #



print("---------\nInicio de sesión\n---------")
contador = 3

while contador >= 1 :

    usuario = input("\nIndique su usuario: ")
    contraseña = input("\nIngrese su contraseña: ")

    if usuario == "estudiante" and contraseña == "hola123":
        contador = 0
        print("\n---------\n¡Ingreso exitoso!\nIniciando sesión...\n---------")
        contador = 0
        
    else:
        contador = contador - 1
        print(f"\n---------\nUsuario o contraseña incorrecta.\n{contador} intentos restantes.\n---------")
        if contador == 0:
            print("¡Cuenta bloqueada!\n---------")


