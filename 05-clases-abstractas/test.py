from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print(f"Creación objeto Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(lado=5, color="rojo")

print(f"Calculo area cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)

print(f"Creación objeto Rectangulo".center(50, "-"))
rect1 = Rectangulo(alto=4, ancho=6, color="azul")
print(f"Calculo area ectangulo: {rect1.calcular_area()}")
print(rect1)

print(Cuadrado.mro())