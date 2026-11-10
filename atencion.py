class Atencion():
    def __init__(self, cita, diagnostico, observaciones):
        self._cita = cita
        self._diagnostico = diagnostico
        self._observaciones = observaciones
        
    def resumen(self):
        return (f"\nFecha : {self._cita._fecha} \nEspecialidad : {self._cita._medico._especialidad} \nPaciente : {self._cita._paciente._nombre}  \nDiagnostico : {self._diagnostico} \nObservaciones : {self._observaciones}")