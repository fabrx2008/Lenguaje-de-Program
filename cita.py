class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha

    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    def resumen(self):
        return (f"\nCita : {self._codigo}  \nFecha : {self._fecha}  \nPaciente : {self._paciente.nombre}  \nMedico : {self._medico.nombre} ({self._medico.especialidad})")