class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)

    def __str__(self):
        return f"{self.nombre} {self.apellido}\n su balance es: {self.balance:.2f} €"

    def depositar(self):
        try:
            cantidad = float(input("¿Cuánto dinero quiere depositar en la cuenta?: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                return
            self.balance += cantidad
            print(f"Se han depositado {cantidad:.2f} €. Nuevo balance: {self.balance:.2f} €")
        except ValueError:
            print("Entrada inválida. Introduzca un número válido.")

    def retirar(self):
        try:
            cantidad = float(input("¿Cuánto dinero desea retirar?: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                return
            if cantidad > self.balance:
                print("Saldo insuficiente.")
            else:
                self.balance -= cantidad
                print(f"Se han retirado {cantidad:.2f} €. Nuevo balance: {self.balance:.2f} €")
        except ValueError:
            print("Entrada inválida. Introduzca un número válido.")

def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl,numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(f"\n🧾 Cliente creado:\n{mi_cliente}")

    opcion = ""

    while opcion != 3:
        print("\n--- MENÚ ---")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mi_cliente.depositar()
        elif opcion == "2":
            mi_cliente.retirar()
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")

inicio()