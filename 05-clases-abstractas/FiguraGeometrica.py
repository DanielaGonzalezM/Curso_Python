from abc import ABC, abstractmethod
# No se puede instanciar una clase abstracta

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self) -> str:
        return f"FiguraGeometrica [Ancho: {self.ancho}, Alto: {self.alto}]"

    def _validar_valor(self, valor):
        if 0 < valor < 10:
            return True
        else:
            print(f" Valor erroneo: {valor}")
            return False