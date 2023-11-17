#proyecto bueno

import random

class Tienda:
    def __init__(self):
        self.registro = {}
        self.productos = {
            "Producto1": {"precio": 10, "stock": 5},
            "Producto2": {"precio": 20, "stock": 10},
            "Producto3": {"precio": 15, "stock": 8},
            "Producto4": {"precio": 25, "stock": 3}
        }
        self.total_compra = 0
        self.productos_seleccionados = []

    def mostrar_menu(self):
        print("\nBienvenido a la Tienda")
        print("1. Registro")
        print("2. Compra")
        print("3. Pago")
        print("4. Salir")

    def registro_usuario(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        # Menú de países
        print("Seleccione su país:")
        paises = ["España", "Francia", "Portugal", "Italia"]
        for i, pais in enumerate(paises, start=1):
            print(f"{i}. {pais}")

        opcion_pais = int(input("Elija un número de país (1-4): "))
        pais = paises[opcion_pais - 1]

        correo_valido = False
        while not correo_valido:
            correo = input("Ingrese su correo electrónico: ")
            if '@' in correo and '.' in correo:
                correo_valido = True
            else:
                print("Correo electrónico no válido. Asegúrese de incluir '@' y '.'.")

        telefono_valido = False
        while not telefono_valido:
            telefono = input("Ingrese su número de teléfono (9 dígitos): ")
            if len(telefono) == 9 and telefono.isdigit():
                telefono_valido = True
            else:
                print("Número de teléfono no válido. Asegúrese de ingresar 10 números.")

        # Guardar datos en el registro
        self.registro = {"nombre": nombre, "apellido": apellido, "pais": pais, "correo": correo, "telefono": telefono}
        print("Registro exitoso.")

    def realizar_compra(self):
        while True:
            print("\nProductos disponibles:")
            for producto, info in self.productos.items():
                print(f"{producto}: ${info['precio']} - Stock: {info['stock']}")

            producto_seleccionado = input("Seleccione un producto para comprar (o escriba 'fin' para salir): ")

            if producto_seleccionado.lower() == 'fin':
                break

            cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado} a comprar: "))

            # Verificar stock suficiente
            if cantidad > self.productos[producto_seleccionado]["stock"]:
                print("Lo siento, no hay suficiente stock disponible.")
                continue

            # Actualizar stock y calcular total
            self.productos[producto_seleccionado]["stock"] -= cantidad
            subtotal = cantidad * self.productos[producto_seleccionado]["precio"]
            self.total_compra += subtotal

            # Agregar a la lista de productos seleccionados
            self.productos_seleccionados.append({
                "producto": producto_seleccionado,
                "cantidad": cantidad,
                "subtotal": subtotal
            })

            '''print(f"\nCompra exitosa:")
            print(f"Producto: {producto_seleccionado}")
            print(f"Cantidad: {cantidad}")
            print(f"Subtotal: ${subtotal}")
            print(f"Total acumulado: ${self.total_compra}")'''

            # Mostrar lista de productos seleccionados
            print("\nProductos seleccionados:")
            for producto in self.productos_seleccionados:
                print(f"{producto['producto']} - Cantidad: {producto['cantidad']} - Subtotal: ${producto['subtotal']}")

    def calcular_impuestos(self):
        # Lógica para calcular impuestos según el país
        # Puedes ajustar esta lógica según tus necesidades
        if self.registro['pais'] == "España":
            return self.total_compra * 0.21
        elif self.registro['pais'] == "Francia":
            return self.total_compra * 0.20
        elif self.registro['pais'] == "Portugal":
            return self.total_compra * 0.23
        elif self.registro['pais'] == "Italia":
            return self.total_compra * 0.22
        else:
            return 0

    def realizar_pago(self):
        # Lógica para realizar el pago
        tarjeta_valida = False
        while not tarjeta_valida:
            numero_tarjeta = input("Ingrese el número de tarjeta (10 dígitos): ")
            if len(numero_tarjeta) == 10 and numero_tarjeta.isdigit():
                tarjeta_valida = True
            else:
                print("Número de tarjeta no válido. Asegúrese de ingresar 10 números.")

        direccion = input("Ingrese su dirección de envío: ")
        print("¡Pago exitoso!")

        # Solicitar factura
        factura = input("¿Desea una factura? (si/no): ").lower()
        if factura == "si":
            opcion_envio = input("¿Desea recibir la factura por correo electrónico o por SMS? (correo/sms): ").lower()
            if opcion_envio == "correo":
                print(f"La factura ha sido enviada a: {self.registro['correo']}")
            elif opcion_envio == "sms":
                print(f"La factura ha sido enviada a: {self.registro['telefono']}")
            else:
                print("Opción de envío no válida. La factura se enviará por correo electrónico por defecto.")

        # Generar número de pedido aleatorio
        numero_pedido = random.randint(1000, 9999)
        print(f"Este es su número de pedido: {numero_pedido}")

        # Mensaje de compra exitosa
        print("\nCompra exitosa:")
        for producto in self.productos_seleccionados:
            print(f"Producto: {producto['producto']} - Cantidad: {producto['cantidad']} - Subtotal: ${producto['subtotal']}")
        print(f"Total acumulado: ${self.total_compra}")

    def ejecutar_tienda(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                self.registro_usuario()

            elif opcion == "2":
                self.realizar_compra()

            elif opcion == "3":
                self.realizar_pago()

            elif opcion == "4":
                print("Gracias por visitar la Tienda. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, elija una opción válida (1-4).")



if __name__ == "__main__":
    tienda = Tienda()
    tienda.ejecutar_tienda()