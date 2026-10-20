
# Sistema de solicitudes académicas de Contacto UPN

from solicitudes import registrar_solicitud, buscar_solicitud


def mostrar_menu():
    print("\n=== SISTEMA DE SOLICITUDES UPN ===")
    print("1. Registrar solicitud")
    print("2. Buscar solicitud")
    print("3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- REGISTRAR SOLICITUD ---")

            codigo = input("Código del estudiante: ")
            nombre = input("Nombre del estudiante: ")
            tipo = input("Tipo de solicitud: ")
            descripcion = input("Descripción de la solicitud: ")

            registrar_solicitud(
                codigo, nombre, tipo, descripcion
            )

        elif opcion == "2":
            print("\n--- BUSCAR SOLICITUD ---")
            codigo = input("Ingrese el código del estudiante: ")
            buscar_solicitud(codigo)

        elif opcion == "3":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    main()
