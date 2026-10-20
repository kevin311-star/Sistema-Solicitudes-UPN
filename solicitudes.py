
# Funciones para gestionar solicitudes académicas

solicitudes = []

def registrar_solicitud(codigo, nombre, tipo, descripcion):
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion
    }

    solicitudes.append(solicitud)
    print("¡Solicitud registrada correctamente!")

def buscar_solicitud(codigo):
    for solicitud in solicitudes:
        if solicitud["codigo"] == codigo:
            print("\n--- SOLICITUD ENCONTRADA ---")
            print(f"Código: {solicitud['codigo']}")
            print(f"Estudiante: {solicitud['nombre']}")
            print(f"Tipo: {solicitud['tipo']}")
            print(f"Descripción: {solicitud['descripcion']}")
            return

    print("No se encontró ninguna solicitud con ese código.")
