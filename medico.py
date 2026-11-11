ESPECIALIDADES_VALIDAS = [
    "Medicina General",
    "Odontologia",
    "Pediatria",
    "Ginecologia Y Obstetricia",
    "Topico",
]


class Medico():
    def __init__(self, codigo, nombre, especialidad):
        self._codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad

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
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        normalizada = str(especialidad).strip().title()
        if normalizada not in ESPECIALIDADES_VALIDAS:
            raise ValueError("La especialidad ingresada no pertenece a la clínica")
        self._especialidad = normalizada

    def resumen(self):
        return (f"\nID : {self._codigo}  \nMedico : {self._nombre}\nEspecialidad : {self._especialidad} ")