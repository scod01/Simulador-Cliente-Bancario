# 🏦 Simulador de Banco en Python

![Portada](portada_cliente_banco.png)

Este proyecto es un simulador básico de cliente bancario desarrollado en Python como práctica de Programación Orientada a Objetos (POO). Permite crear un cliente, depositar y retirar dinero, todo a través de una interfaz de consola.

---

## 🧩 Estructura del código

- `Persona`: clase base que contiene nombre y apellido.
- `Cliente`: hereda de `Persona` e incluye número de cuenta y balance.
- Métodos:
  - `depositar()`: permite ingresar dinero.
  - `retirar()`: permite extraer dinero si hay saldo suficiente.
  - `__str__()`: muestra el estado del cliente.
- `crear_cliente()`: crea una instancia de cliente con entrada del usuario.
- `inicio()`: menú interactivo por consola.

---

## ⚙️ Cómo ejecutar el programa

1. Asegúrate de tener Python instalado (recomendado 3.7 o superior).
2. Descarga o clona este repositorio.
3. Ejecuta el archivo principal desde terminal o consola:

```bash
python cliente_banco.py

## 👨‍💻 Autor

**David Suárez**
[GitHub](https://github.com/scod01)
[LinkedIn](www.linkedin.com/in/david.suarez-dev)
