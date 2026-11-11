class Paciente():
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self.nombre = nombre
        self.edad = edad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre.strip()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if edad <= 0 or edad >= 120:
            raise ValueError("La edad no puede ser menor igual a 0 o mayor igual a 120")
        self._edad = edad

    def resumen(self):
        return (f"\nID : {self._codigo}  \nPaciente : {self._nombre}  \nEdad : {self._edad} ")
