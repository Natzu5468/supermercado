# miembros/zbotones/inicio.py
import tkinter as tk

def mostrar_inicio():
    texto_inicio = """
Bienvenido al sistema de supermercado virtual

"Descubre nuestra nueva página de supermercado virtual, donde encontrarás una amplia selección de productos frescos y de calidad desde la comodidad de tu hogar. Disfruta de envíos rápidos, promociones exclusivas y una experiencia de compra segura y conveniente, diseñada para ahorrar tiempo y dinero."
Si necesitas ayuda en cualquier momento, no dudes en utilizar las siguientes opciones de soporte:

servicio de productos : Explora nuestro catálogo en línea para encontrar produtos disponibles en nuestra sucursal.
"""
    return texto_inicio

def crear_botones_inicio(frame):
    button_inicio = tk.Button(frame, text="Inicio", font=("Arial", 18), bg="#A8C3A6", fg="white")
    button_inicio.pack(fill="x", pady=20)

    return button_inicio