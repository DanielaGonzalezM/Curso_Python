from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, "rojo")

print(f"Calculo area cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)

rect1 = Rectangulo(4, 6, "azul")
print(f"Calculo area ectangulo: {rect1.calcular_area()}")
print(rect1)
