print("ejercicio 1")
print("")
for i in range(1,11,2):
  print(i)
print("")
print("Ejercicio 2")
print("")

x = 0
while x < 10:
  if x % 2 !=0:
    print(x)
  x+=1
print("")
print("Ejercicio 3")
print("")



contra = "chupacabra"

while  True:
  password = input("Ingrese contraseña ")
  if password == contra:
    print("contraseña correcta!")
    break 
  print("Contraseña incorrecta ingrese de nuevo la contraseña")
  
print("")
print("Ejercicio 4")
print("")
palabra = input("ingrese cualquier palabra ")
palabra = palabra.upper()

for letter in palabra:
  if letter in "AEIOU":
    continue
  print(letter)