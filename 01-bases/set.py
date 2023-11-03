nombres = {"Daniela", "Canela", "Ceniza"}
# No guarda orden
print(nombres)
print(len(nombres))

print("Daniela" in nombres)

# No soporta duplicados
nombres.add("add")
nombres.add("add")
print(nombres)
nombres.remove("add")
print(nombres)
#Eliminar sin error si no existe
nombres.discard("ff")
print(nombres)
nombres.clear()
print(nombres)
