def myFunc(text):
    print("hola", text)


myFunc("test")


def suma(a=0, b=0) -> int:
    return a+b


print(suma(2, 5))
print(f"Resultado suma: {suma(3)}")


def listaNombres(*args):
    for nombre in args:
        print(nombre)


nombs = ("Daniela", "Canela", "Ceniza")
listaNombres(nombs)


def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")


listarTerminos(key1="test1", key2="test2")
