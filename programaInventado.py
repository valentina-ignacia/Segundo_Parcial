#Se debe desarrollar un programa que simule un sistema de login de usuarios. Este debe permitir iniciar sesión registrarse y salir, mediante un menú interactivo. Se debe utilizar un diccionario para almacenar usuarios con sus contraseñas, verificando que estos usuarios no se repitan. El programa debe validar que el usuario exista y que la contraseña sea correcta. Se debe permitir hasta 3 intentos al ingresar la contraseña, cuando se cumplan esos 3 intentos, debe decir que la cuenta está bloqueada.



print("------------\n¡Bienvenid@!\n------------")



# Almacenamiento de usuarios y contraseñas

usuarios = {"valentina" : "hola123"}



# Menú 

while True:

  print("\n1. Iniciar sesión\n2. Registrarse\n3. Salir")

  opcion = input("\nSeleccione una opción: ")



  # Opción inválida



  while opcion != "1" and opcion != "2" and opcion != "3":

    print("¡Opción inválida!\nIntente nuevamente.")

    opcion = input("Seleccione una opción: ")



  # 1. Iniciar sesión



  if opcion == "1":

    contador = 3



    print("------------\nInicio de sesión\n------------")

    while contador > 0:

      nombre = input("\nIngrese su nombre de usuario: ").lower()

      contraseña = input("Ingrese su contraseña: ")



      if nombre in usuarios and usuarios[nombre] == contraseña:

        print(f"\n¡Bienvenid@ {nombre.capitalize()}!\nIniciando sesión...")

        exit()

      else:

        contador -= 1

        print(f"\n¡Datos incorrectos!\nLe quedan {contador} intentos")

    

    if contador == 0:

      print("\n¡No le quedan más intentos!\nCuenta bloqueada.")

      



  # 2.Registrarse



  elif opcion == "2":



    while True:

      nuevo = input("\nElija su nombre de usuario: ").lower()



      if nuevo in usuarios:

        print("\nNombre de usuario ya existente.\nIntente con otro: ")

        continue

      

      else:

        nueva_contra = input("Escriba su contraseña: ")



        usuarios[nuevo] = nueva_contra

        print("¡Usuario registrado!")

        break



  # 3.Salir

  

  elif opcion == "3":

    print("Sistema finalizado.")

    break