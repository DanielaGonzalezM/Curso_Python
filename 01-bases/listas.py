nombres = ["Daniela", "Canela", "Ceniza"]

print(nombres)
print(nombres[0])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2])
print(nombres[:2])
print(len(nombres))

nombres.append("append")
print(nombres)
nombres.insert(1,"insert")
print(nombres)

nombres.remove("insert")
print(nombres)
nombres.pop()
print(nombres)

del nombres[0]
print(nombres)

nombres.clear()
print(nombres)
