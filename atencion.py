class Atencion():
    def __init__(self, cita, diagnostico, observaciones):
        self._cita = cita
        self._diagnostico = diagnostico
        self._observaciones = observaciones

    def resumen(self):
        return (f"\nFecha : {self._cita.fecha}"
                f"\nEspecialidad : {self._cita.medico.especialidad}"
                f"\nPaciente : {self._cita.paciente.nombre}"
                f"\nDiagnostico : {self._diagnostico}"
                f"\nObservaciones : {self._observaciones}")
