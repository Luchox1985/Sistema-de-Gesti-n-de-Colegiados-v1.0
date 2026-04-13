# 1. DATOS — lista de 3 usuarios
usuarios = [
    {"rut": "11111111-1", "nombre": "Ana García",  "estado": "ACTIVO"},
    {"rut": "22222222-2", "nombre": "Luis Pérez",  "estado": "MOROSO"},
    {"rut": "33333333-3", "nombre": "María López", "estado": "INACTIVO"},
    {"rut": "44444444-4", "nombre": "Lalo Landa", "estado": "FALLECIDO"}
]

# 2. FUNCIÓN — recibe UN usuario y muestra sus datos
def mostrar_usuario(usuario):
    print(f"RUT: {usuario['rut']} | Nombre: {usuario['nombre']} | Estado: {usuario['estado']}")
    if usuario["estado"] == "MOROSO":
        print("⚠ Requiere gestión de cobranza")

    elif usuario["estado"] == "INACTIVO":
        print("📋 Revisar reincorporación")

    elif usuario["estado"] == "FALLECIDO":
        print("🔴 Dar de baja del sistema")

# 3. FOR — llama la función para CADA usuario de la lista
for usuario in usuarios:
    mostrar_usuario(usuario)

print(f"\nTotal usuarios: {len(usuarios)}")
