from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion


def cargar_datos_prueba(sistema):
    # Datos ya registrados al iniciar (sin imprimir nada por consola)
    sistema.crear_persona("paciente", "Jorgue Aguayo", 28)
    sistema.crear_persona("paciente", "Rosa Quispe", 14)
    sistema.crear_persona("paciente", "Marixa Segarra", 18)
    sistema.crear_persona("paciente", "Fernando Torres", 30)

    sistema.crear_persona("medico", "Marcos Fernandez", "Medicina General")
    sistema.crear_persona("medico", "Raul Torres", "Odontologia")
    sistema.crear_persona("medico", "Pablo Hernandez", "Pediatria")
    sistema.crear_persona("medico", "Rosa Maria", "Pediatria")
    sistema.crear_persona("medico", "Juliana Rivera", "Ginecologia y Obstetricia")
    sistema.crear_persona("medico", "Karla Rosales", "Topico")

    sistema.programar_cita("P001", "M002", "2026/10/5")
    sistema.programar_cita("P001", "M001", "2026/10/12")
    sistema.programar_cita("P002", "M002", "2026/10/20")
    sistema.programar_cita("P002", "M003", "2026/11/8")

    sistema.registrar_atencion("C001", "Caries leve", "Se realiza curación simple con resina.")
    sistema.registrar_atencion("C002", "Faringitis aguda", "Se recetan antibioticos y descanso por 5 dias.")
    sistema.registrar_atencion("C003", "Gingivitis", "Se realiza profilaxis dental y se recomienda uso de hilo dental.")
    sistema.registrar_atencion("C004", "Control de adol", "Se realiza profilaxis dental y se recomienda uso de hilo dental.")


class SistemaKawsay:
    def __init__(self):
        self.pacientes = {}
        self.medicos = {}
        self.citas = {}
        self.historial_atenciones = []
        self.citas_atendidas = []

        cargar_datos_prueba(self)

    def _siguiente_codigo(self, prefijo, diccionario):
        """Genera el siguiente código automáticamente: P001, P002, M001, C001, etc."""
        numeros = []
        for codigo in diccionario.keys():
            if codigo.startswith(prefijo):
                try:
                    numeros.append(int(codigo[len(prefijo):]))
                except ValueError:
                    pass
        siguiente = max(numeros) + 1 if numeros else 1
        return f"{prefijo}{siguiente:03d}"

    def buscar_por_codigo(self, codigo):
        if codigo in self.pacientes:
            return self.pacientes[codigo]
        elif codigo in self.medicos:
            return self.medicos[codigo]
        return None

    def crear_persona(self, tipo, nombre, dato_extra):
        if tipo == "paciente":
            codigo = self._siguiente_codigo("P", self.pacientes)
            nuevo = Paciente(codigo, nombre, dato_extra)
            self.pacientes[codigo] = nuevo
            return codigo, nuevo
        elif tipo == "medico":
            codigo = self._siguiente_codigo("M", self.medicos)
            nuevo = Medico(codigo, nombre, dato_extra)
            self.medicos[codigo] = nuevo
            return codigo, nuevo
        else:
            raise ValueError("Tipo no válido")

    def programar_cita(self, cod_paciente, cod_medico, fecha):
        paciente = self.buscar_por_codigo(cod_paciente)
        medico = self.buscar_por_codigo(cod_medico)

        if not isinstance(paciente, Paciente) or not isinstance(medico, Medico):
            raise ValueError("Referencia no encontrada")

        cod_cita = self._siguiente_codigo("C", self.citas)
        nueva_cita = Cita(cod_cita, paciente, medico, fecha)
        self.citas[cod_cita] = nueva_cita
        return cod_cita, nueva_cita

    def registrar_atencion(self, cod_cita, diagnostico, observaciones):
        if cod_cita not in self.citas:
            raise KeyError("El código de cita no existe")

        if cod_cita in self.citas_atendidas:
            raise ValueError("Esta cita ya tiene una atención registrada")

        cita = self.citas[cod_cita]
        nueva_atencion = Atencion(cita, diagnostico, observaciones)
        self.historial_atenciones.append(nueva_atencion)
        self.citas_atendidas.append(cod_cita)
        return nueva_atencion

    def filtrar_medicos_por_especialidad(self, especialidad):
        medicos_filtrados = filter(
            lambda medico: medico.especialidad.lower() == especialidad.lower(),
            self.medicos.values(),
        )
        return list(medicos_filtrados)