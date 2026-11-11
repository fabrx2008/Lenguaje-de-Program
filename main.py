from sistema_kawsay import SistemaKawsay
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

    opcion = input("Seleccione una opcion : ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente : ")

        try:
            edad = int(input("Ingrese su edad : "))
            codigo, paciente = sistema.crear_persona("paciente", nombre, edad)
            print(f"Paciente registrado con éxito. Código: {codigo}")
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                print("Error: La edad debe ser un numero entero.")
            else:
                print(f"Error : {e}")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del medico : ")

        especialidades_validas = ["Medicina General", "Odontologia", "Pediatria", "Ginecologia Y Obstetricia", "Topico"]

        print(f"\nEspecialidades válidas: {', '.join(especialidades_validas)}")
        especialidad = input("Ingrese su especialidad : ").title()

        if especialidad not in especialidades_validas:
            print("Error: La especialidad ingresada no pertenece a la clínica.")
            continue

        codigo, medico = sistema.crear_persona("medico", nombre, especialidad)
        print(f"Médico creado con éxito. Código: {codigo}")

    elif opcion == "3":
        codigo = input("Ingrese el codigo a buscar : ").upper()

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

        cod_pac = input("\nCódigo del paciente: ").upper()
        cod_med = input("Código del médico: ").upper()
        fecha = input("Fecha (YYYY-MM-DD): ")

        try:
            cod_cita, cita = sistema.programar_cita(cod_pac, cod_med, fecha)
            print(f"Cita programada exitosamente. Código: {cod_cita}")
        except ValueError as e:
            print(f"Error al programar la cita: {e}")

    elif opcion == "5":
        cod_cita = input("Ingrese el codigo de la cita atendida : ").upper()
        diagnostico = input("Ingrese el diagnostico : ")
        observaciones = input("Ingrese observaciones : ")

        try:
            sistema.registrar_atencion(cod_cita, diagnostico, observaciones)
            print("Atención registrada en el historial correctamente.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    elif opcion == "6":
        if not sistema.historial_atenciones:
            print("El historial esta vacio")
        else:
            print("\n--- HISTORIAL CLINICO ---")
            for atencion in sistema.historial_atenciones:
                print(atencion.resumen())

    elif opcion == "7":
        especialidades_validas = [
            "Medicina General",
            "Odontologia",
            "Pediatria",
            "Ginecologia Y Obstetricia",
            "Topico"
        ]

        print("\n--- ESPECIALIDADES DISPONIBLES ---")
        for especialidad in especialidades_validas:
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