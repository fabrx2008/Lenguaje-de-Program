class Medico():
    def __init__(self,codigo,nombre,especialidad):
        self._codigo = codigo
        self._nombre = nombre
        self._especialidad = especialidad
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def especialidad(self):
        return self._especialidad
        
    def resumen(self):
        return (f"\nID : {self._codigo}  \nMedico : {self._nombre}\nEspecialidad : {self._especialidad} ")