from sistema_kawsay import SistemaKawsay
from medico import ESPECIALIDADES_VALIDAS

sistema = SistemaKawsay()

while True:
    print("\n--- SISTEMA KAWSAY ---")
    print("1. Registrar Paciente")
    print("2. Registrar Médico")
    print("3. Buscar por Código")
    print("4. Programar Cita")
    print("5. Registrar Atención")
    print("6. Ver Historial de Atenciones")
    print("7. Buscar Medico por especialidad")
    print("8. Salir")

    opcion = input("Seleccione una opcion : ").strip()

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente : ")

        try:
            edad = int(input("Ingrese su edad : "))
        except ValueError:
            print("Error: La edad debe ser un numero entero.")
            continue

        try:
            codigo, paciente = sistema.crear_persona("paciente", nombre, edad)
            print(f"Paciente registrado con éxito. Código: {codigo}")
        except ValueError as e:
            print(f"Error : {e}")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del medico : ")

        print(f"\nEspecialidades válidas: {', '.join(ESPECIALIDADES_VALIDAS)}")
        especialidad = input("Ingrese su especialidad : ")

        try:
            codigo, medico = sistema.crear_persona("medico", nombre, especialidad)
            print(f"Médico creado con éxito. Código: {codigo}")
        except ValueError as e:
            print(f"Error : {e}")

    elif opcion == "3":
        codigo = input("Ingrese el codigo a buscar : ").strip().upper()

        resultado = sistema.buscar_por_codigo(codigo)

        if resultado:
            print(f"\nCodigo encontrado :{resultado.resumen()}")
        else:
            print("Codigo no encontrado en el sistema.")

    elif opcion == "4":
        print("\n--- PACIENTES REGISTRADOS ---")
        if sistema.pacientes:
            for paciente in sistema.pacientes.values():
                print(paciente.resumen())
        else:
            print("No hay pacientes registrados.")

        print("\n--- MÉDICOS REGISTRADOS ---")
        if sistema.medicos:
            for medico in sistema.medicos.values():
                print(medico.resumen())
        else:
            print("No hay médicos registrados.")

        cod_pac = input("\nCódigo del paciente: ").strip().upper()
        cod_med = input("Código del médico: ").strip().upper()
        fecha = input("Fecha (YYYY-MM-DD): ")

        try:
            cod_cita, cita = sistema.programar_cita(cod_pac, cod_med, fecha)
            print(f"Cita programada exitosamente. Código: {cod_cita}")
        except ValueError as e:
            print(f"Error al programar la cita: {e}")

    elif opcion == "5":
        pendientes = sistema.filtrar_citas_pendientes()
        if not pendientes:
            print("No hay citas pendientes de atención.")
            continue

        print("\n--- CITAS PENDIENTES ---")
        for cita in pendientes:
            print(cita.resumen())

        cod_cita = input("\nIngrese el codigo de la cita atendida : ").strip().upper()
        diagnostico = input("Ingrese el diagnostico : ")
        observaciones = input("Ingrese observaciones : ")

        try:
            sistema.registrar_atencion(cod_cita, diagnostico, observaciones)
            print("Atención registrada en el historial correctamente.")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "6":
        if not sistema.historial_atenciones:
            print("El historial esta vacio")
        else:
            print("\n--- HISTORIAL CLINICO ---")
            for atencion in sistema.historial_atenciones:
                print(atencion.resumen())

    elif opcion == "7":
        print("\n--- ESPECIALIDADES DISPONIBLES ---")
        for especialidad in ESPECIALIDADES_VALIDAS:
            print(f"- {especialidad}")

        especialidad_buscada = input("\nIngrese la especialidad a buscar: ").strip().title()
        resultados = sistema.filtrar_medicos_por_especialidad(especialidad_buscada)

        if resultados:
            print(f"\n--- Médicos encontrados ({especialidad_buscada}) ---")
            for med in resultados:
                print(med.resumen())
        else:
            print("No se encontraron médicos con esa especialidad.")

    elif opcion == "8":
        print("Cerrando prototipo kawsay")
        break
    else:
        print("Opcion invalida")
