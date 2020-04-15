nombre = input("Ingresa tu nombre: ")
letras = len(nombre)
letras = str(letras)

#Recordar que solo se concatenan str , por eso la conversion previa del int letras
print(nombre+" tiene "+letras+" letras.")