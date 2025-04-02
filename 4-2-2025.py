Exelente = 0
MBueno = 0
bueno = 0
regular = 0
Malo = 0
total = 0
resMenores = 0
person = []
resultados = []
numeroP = int(input("¿Cuántas personas van a llenar la encuesta? "))
print("En base a la experiencia que tuvo el día de hoy, ¿cómo calificaría el servicio siendo 5 Excelente y 1 Malo?")
for encuesta in range(1, numeroP + 1):
    Survey = input(f"Resultado encuesta {encuesta} (1-5): ")
    person.append(encuesta)
    resultados.append(Survey)
    match Survey:  
        case "1":
            Malo += 1
            total += 1
            resMenores += 1
        case "2":
            regular += 1
            total += 2
            resMenores += 1
        case "3":
            bueno += 1
            total += 3
        case "4":
            MBueno += 1
            total += 4
        case "5":
            Exelente += 1
            total += 5
        case _:  
            print("Respuesta no válida. Por favor, ingrese un número entre 1 y 5.")
            resultados.pop() 
            person.pop()  
            continue

promedio = total / len(resultados) if resultados else 0  
print("El promedio de satisfacción es de:", promedio)
print("La respuesta más frecuente fue:", max(set(resultados), key=resultados.count))
print("el porcentage menor al promedio fue de ", (resMenores/numeroP)*100)
print("encuestas Exelentes ", Exelente)
print("encuestas Muy Buenas ", MBueno)
print("Encuentas Buenas ", bueno)
print("encuestas regulares " , regular)
print("Encuestas Malas " , Malo) 


