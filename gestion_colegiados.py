# Variable de control — empieza vacía para que el while arranque de inmediato
opcion = ""

# Base de datos simulada — en v2.0 esto vendrá directo desde el Excel real
colegiados = [
    {"rut": "111-1", "nombre": "Ana García",  "estado": "ACTIVO"},
    {"rut": "222-2", "nombre": "Luis Pérez",  "estado": "MOROSO"},
    {"rut": "333-3", "nombre": "María López", "estado": "INACTIVO"},
    {"rut": "444-4", "nombre": "Juan Soto",   "estado": "ACTIVO"},
    {"rut": "555-5", "nombre": "Rosa Muñoz",  "estado": "MOROSO"}
]

# Muestra todos los colegiados sin filtro — útil para ver el panorama completo
def ver_colegiados(lista):
    print("\n--- LISTA DE COLEGIADOS ---")
    for c in lista:
        print(f"{c['rut']} | {c['nombre']} | {c['estado']}")
    print(f"Total: {len(lista)}")

# Filtra solo los morosos — los que requieren gestión de cobranza
def ver_morosos(lista):
    print("\n--- COLEGIADOS MOROSOS ---")
    for c in lista:
        if c["estado"] == "MOROSO":
            print(f"{c['rut']} | {c['nombre']}")

# Filtra solo los activos — los que están al día con sus cuotas
def ver_activos(lista):
    print("\n--- COLEGIADOS ACTIVOS ---")
    for c in lista:
        if c["estado"] == "ACTIVO":
            print(f"{c['rut']} | {c['nombre']}")

# El menú corre indefinidamente hasta que el usuario elija 0
# El while se rompe solo cuando opcion == "0" — sin necesidad de break
while opcion != "0":
    print("==================")
    print("  MENÚ PRINCIPAL  ")
    print("==================")
    print("1. Ver colegiados")
    print("2. Ver morosos")
    print("3. Ver activos")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    # Cada opción llama su función correspondiente
    # El menú no tiene lógica propia — solo deriva al lugar correcto
    if opcion == "1":
        ver_colegiados(colegiados)
    elif opcion == "2":
        ver_morosos(colegiados)
    elif opcion == "3":
        ver_activos(colegiados)
    elif opcion == "0":
        print("¡Hasta luego!")
    else:
        # Si el usuario escribe cualquier otra cosa, le avisamos y volvemos al menú
        print("Opción no válida. Intenta de nuevo.")
