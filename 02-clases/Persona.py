class Persona:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre  # doble __ no se puede modificar
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(self._nombre, self._apellido, self._edad)

    def __del__(self):
        print(f"eliminando {self._nombre}")

if __name__ == "__main__":

    persona = Persona("t", "rr", 23)
    persona.mostrar_detalle()

    persona.telefono = 123
    print(persona.telefono)
    Persona.mostrar_detalle(persona)

    persona.nombre = "test"  # llama indirectamente al set
    print(persona.nombre)
    persona.mostrar_detalle()
