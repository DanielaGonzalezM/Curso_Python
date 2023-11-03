cadena = "Holi"

for letra in cadena:
    if letra == "o":
        continue
    print(letra, end=" - ")
    if letra == "l":
        break
else:
    print("fin")
