nuemro = int(input("Ingrese un numero: del 1-9 "))
resultado = 0  
if nuemro <= 3:
    resultado= nuemro*"I"
elif nuemro == 4:
    resultado= "IV"
elif nuemro == 5:
    resultado= "V"
elif nuemro <= 8:
    resultado= "V"+(nuemro-5)*"I"
elif nuemro == 9:
    resultado= "IX"
else:
    print("numero no valido")
print(f"el numero romano de {nuemro} es {resultado}")