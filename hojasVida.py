ofertas = []
candidatos = []
perfiles = []

print("====== SISTEMA DE INFORMACIÓN LABORAL ======")
print("1. Registrar una oferta laboral")
print("2. Registrar un candidato (hoja de vida)")
print("3. Agregar un perfil laboral")
print("4. Ver todo lo registrado")
print("5. Salir")

opcion = input("Seleccione una opción (1-5): ")

while opcion != "5":
    if opcion == "1":
        print("=== Registrar una oferta laboral ===")
        titulo = input("Título del puesto: ")
        empresa = input("Nombre de la empresa: ")
        salario = input("Salario ofrecido: ")
        descripcion = input("Descripción del cargo: ")
        
        oferta = {
            "titulo": titulo,
            "empresa": empresa,
            "salario": salario,
            "descripcion": descripcion
        }
        
        ofertas.append(oferta)
        print("✅ Oferta registrada con éxito.\n")

    elif opcion == "2":
        print("=== Registrar un candidato (hoja de vida) ===")
        nombre = input("Nombre completo: ")
        edad = input("Edad: ")
        profesion = input("Profesión: ")
        experiencia = input("Años de experiencia: ")
        
        candidato = {
            "nombre": nombre,
            "edad": edad,
            "profesion": profesion,
            "experiencia": experiencia
        }
        
        candidatos.append(candidato)
        print("✅ Candidato registrado con éxito.\n")

    elif opcion == "3":
        print("=== Agregar un perfil laboral ===")
        nombre_perfil = input("Nombre del perfil laboral: ")
        habilidades = input("Lista de habilidades (separadas por coma): ")
        sector = input("Sector laboral: ")

        perfil = {
            "nombre_perfil": nombre_perfil,
            "habilidades": habilidades.split(","),
            "sector": sector
        }

        perfiles.append(perfil)
        print("✅ Perfil laboral agregado con éxito.\n")

    elif opcion == "4":
        print("=== Datos Registrados ===")
        print("\n--- Ofertas Laborales ---")
        for o in ofertas:
            print(o)

        print("\n--- Candidatos ---")
        for c in candidatos:
            print(c)

        print("\n--- Perfiles Laborales ---")
        for p in perfiles:
            print(p)

        print("")

    else:
        print("❌ Opción no válida. Intenta otra vez.")

        print("====== MENÚ PRINCIPAL ======")
    print("1. Registrar una oferta laboral")
    print("2. Registrar un candidato (hoja de vida)")
    print("3. Agregar un perfil laboral")
    print("4. Ver todo lo registrado")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

print("👋 Programa finalizado.")
