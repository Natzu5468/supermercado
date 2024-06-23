import tkinter as tk
from tkinter import messagebox
from botones_secundarios.boton_agregar_miembros import miembros_lista

prestamos_activos = []

def mostrar_prestamo(frame, root):
    def on_generar_factura():
        if combo_eres_miembro.get() == "Sí":
            miembro_seleccionado = combo_miembros.get()
            cedula_confirmacion = entry_cedula_confirmacion.get().strip()
            if not miembro_seleccionado or not cedula_confirmacion:
                messagebox.showerror("Error", "Todos los campos deben estar llenos")
                return
            
            # Registrar el préstamo
            prestamo_info = {
                "miembro": miembro_seleccionado,
                "cedula_confirmacion": cedula_confirmacion
            }
            prestamos_activos.append(prestamo_info)
            messagebox.showinfo("Éxito", "Factura generada con éxito")
        
        # Limpiar los campos después de generar la factura
        combo_eres_miembro.set('')
        combo_miembros.set('')
        entry_cedula_confirmacion.delete(0, tk.END)

    for widget in frame.winfo_children():
        widget.destroy()

    label_instrucciones = tk.Label(frame, text="Para aprobar la compra, complete la siguiente información:", font=("Arial", 14))
    label_instrucciones.pack(pady=10)

    # Pregunta "Eres miembro"
    tk.Label(frame, text="¿Eres miembro?", font=("Arial", 12)).pack(anchor="w", padx=20)
    combo_eres_miembro = tk.StringVar()
    combo_eres_miembro.set('')  # Valor inicial vacío
    combo_eres_miembro_dropdown = tk.OptionMenu(frame, combo_eres_miembro, "Sí", "No")
    combo_eres_miembro_dropdown.pack(fill="x", padx=20, pady=5)
    
    # Condición para mostrar los campos de miembro solo si se selecciona "Sí"
    def mostrar_campos_miembro(*args):
        if combo_eres_miembro.get() == "Sí":
            tk.Label(frame, text="Miembro:", font=("Arial", 12)).pack(anchor="w", padx=20)
            combo_miembros.set('')  # Valor inicial vacío
            combo_miembros_dropdown = tk.OptionMenu(frame, combo_miembros, *miembros_lista)
            combo_miembros_dropdown.pack(fill="x", padx=20, pady=5)
            
            tk.Label(frame, text="Confirmación de cédula:", font=("Arial", 12)).pack(anchor="w", padx=20)
            entry_cedula_confirmacion.pack(fill="x", padx=20, pady=5)

    combo_eres_miembro.trace('w', mostrar_campos_miembro)
    
    # Variables para campos de miembro
    combo_miembros = tk.StringVar()
    entry_cedula_confirmacion = tk.Entry(frame, font=("Arial", 12))
    
    # Botón para generar factura
    button_generar_factura = tk.Button(frame, text="Generar Factura", font=("Arial", 14), command=on_generar_factura)
    button_generar_factura.pack(pady=20)