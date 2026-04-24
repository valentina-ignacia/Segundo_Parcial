print("-----------------------\nCajero Banco Santander\n-----------------------")

rut = input("\n¡Bienvenid@!\nIngrese su RUT (con dígito verificador): ")



while rut.isalpha() == True or "." in rut or len(str(rut)) < 10 or len(str(rut)) > 10:

  print("\n¡RUT inválido!")

   

  if rut.isalpha() == True:

    print("El RUT no debe contener letras.")

  elif "." in rut:

    print("El RUT no debe tener puntos.")

  else:

    print("Cantidad de dígitos incorrectos.")

  rut = input("Intente nuevamente: ")

   



clave = input("\nIngrese su clave (no debe ser mayor a 10 dígitos): ")

   

while len(str(clave)) > 10:

  print("\n¡Clave inválida!\nLa clave ingresada no debe tener más de 10 dígitos.")

  clave = input("Intente nuevamente: ")

     

   

if "-" in rut and len(rut) == 10 and len(str(clave)) <= 10:

  print("\n-----------------------\n¡Datos validados correctamente!\nIngresando...\n-----------------------")

