import tkinter as tk
from tkinter import messagebox

categorias_libros = {
    "Frescos": [("Leche entera, 1 litro", "$3,500"),
        ("Huevos, docena", "$8,000"),
        ("Tomates, kilogramo" , "$4,500"),
        ("Pechuga de pollo, kilogramo" , "$12,000"),
        ("Manzanas, kilogramo " , "$6,000"),
        ("Queso mozzarella, 200g" , "$5,200"),
        ("Pan integral, unidad" , "$3,000"),
        ("Yogurt natural, 500ml" ,"$2,800"),
        ("Aguacates, unidad ", "$2,500"),
        ("Papas, kilogramo" , "$2,200"),
    ],
    "Platos preparados": [
        ("Pizza margarita, tamaño familiar", "$18,000"),
        ("Sushi surtido, 20 piezas" , "$35,000"),
        ("Ensalada César, porción individual", "$10,000"),
        ("Lasagna de carne, 1 bandeja", "$22,000"),
        ("Empanadas de carne, 6 unidades" ,"$12,000"),
        ("Pollo asado con papas, 1 porción" , "$15,000"),
        ("Hamburguesa gourmet, con papas fritas", "$20,000"),
        ("Sándwich de pollo, tipo club", "$8,000"),
        ("Rollitos primavera, 10 unidades", "$14,000"),
        ("Paella mixta, 1 porción" ,"$25,000"),
    ],
    
    "despensa": [  
        ("Arroz blanco, kilogramo" , "$4,000"),
        ("Frijoles rojos, kilogramo" , "$6,500"),
        ("Pasta de trigo, 500g" , "$2,800"),
        ("Aceite de cocina, litro" , "$9,000"),
        ("Azúcar blanca, kilogramo" , "$3,500"),
        ("Harina de maíz, kilogramo" , "$3,200"),
        ("Salsa de tomate, frasco 500g" , "$4,500"),
        ("Café colombiano, 250g" , "$8,000"),
        ("Atún en lata, 200g" , "$5,500"),
        ("Galletas de soda, paquete" , "$2,000"),
    ],
    
    "Mascotas": [
        ("Alimento para perros, 2kg" , "$15,000"),
        ("Arena para gatos, 5kg" , "$18,000"),
        ("Juguetes para perros, unidad" , "$7,000"),
        ("Comedero automático para gatos" , "$25,000"),
        ("Champú para perros, 500ml" , "$10,000"),
        ("Collar antipulgas para gatos" , "$12,000"),
        ("Golosinas para perros, paquete ", "$4,500"),
        ("Cama para mascotas pequeñas ", "$30,000"),
        ("Piedras sanitarias para gatos, 10kg" , "$22,000"),
        ("Correa retráctil para perros" , "$15,000"),
    ],
    "Bebé": [
        ("Pañales desechables, paquete 40 unidades" , "$25,000"),
        ("Fórmula infantil, lata 800g" , "$30,000"),
        ("Toallitas húmedas, paquete 80 unidades" , "$8,000"),
        ("Crema para rozaduras, 100g" , "$5,500"),
        ("Biberones de vidrio, unidad" , "$12,000"),
        ("Ropa de bebé (pijama), unidad" , "$18,000"),
        ("Silla para carro infantil" , "$150,000"),
        ("Cuna portátil" , "$180,000"),
        ("Juguete de peluche para bebé" , "$15,000"),
        ("Termómetro digital para bebé" , "$20,000"),
    ],  
    "Cuidado del hogar": [
        ("Detergente líquido, 2 litros" , "$12,000"),
        ("Limpiavidrios en aerosol, 500ml" , "$7,000"),
        ("Esponjas para lavar platos, paquete" , "$3,500"),
        ("Ambientador en spray, 300ml" , "$5,000"),
        ("Bolsas de basura, paquete 20 unidades" , "$6,000"),
        ("Quitamanchas en gel, 500ml" , "$9,000"),
        ("Papel higiénico, paquete 4 rollos" , "$5,500"),
        ("Escoba y recogedor, juego" , "$15,000"),
       ("Mopa con cubo exprimidor" , "$20,000"),
        ("Jabón para lavar ropa, kilogramo" , "$6,500"),
    ], 
    "Cuidado personal": [
        ("Champú hidratante, 400ml" , "$8,000"),
        ("Crema facial humectante, 50g" , "$12,000"),
        ("Gel de ducha, 500ml" , "$6,000"),
        ("Desodorante antitranspirante, 100ml" , "$5,000"),
        ("Pasta dental, 100g" , "$3,500"),
        ("Maquinilla de afeitar desechable, paquete 5 unidades" , "$10,000"),
        ("Toallas sanitarias, paquete 10 unidades" , "$4,000"),
        ("Crema para manos, 100ml" , "$4,500"),
        ("Protector solar FPS 50, 150ml" , "$18,000"),
        ("Cortauñas con lima" , "$2,500"),
    ],
    "Bebidas y bodega":[
        ("Vino tinto reserva, botella" , "$50,000"),
        ("Cerveza artesanal, pack 6 unidades" , "$30,000"),
       ("Refresco de cola, botella 2 litros" , "$5,000"),
        ("Agua mineral sin gas, botella 1.5 litros" , "$2,000"),
        ("Whisky escocés, botella 750ml" , "$150,000"),
        ("Jugo de naranja natural, litro" , "$6,000"),
        ("Café instantáneo, frasco 200g" , "$10,000"),
        ("Tequila blanco, botella 750ml" , "$80,000"),
        ("Sidra de manzana, botella 750ml" , "$25,000"),
        ("Vermut blanco, botella 750ml" , "$35,000"),
    ]
}

def agregar_categoria(frame):
    def on_agregar_click():
        nombre_categoria = entry_nombre_categoria.get().strip()
        libros_info = []

        # Validación de nombre de categoría
        if not nombre_categoria or nombre_categoria.isdigit():
            messagebox.showerror("Error", "El nombre de la categoría debe contener al menos un carácter y no puede ser numérico")
            return

        # Validación de libros
        libros_existentes = set()
        for libros in categorias_libros.values():
            for libro, _ in libros:
                libros_existentes.add(libro.lower())

        for i in range(5):
            nombre_libro = entry_libros[i].get().strip()
            cantidad_libro = entry_cantidad[i].get().strip()
            if not nombre_libro or not cantidad_libro:
                messagebox.showerror("Error", "Todos los campos de nombre de libro y cantidad deben estar llenos")
                return
            if nombre_libro.lower() in libros_existentes:
                messagebox.showerror("Error", f"El nombre del libro '{nombre_libro}' ya existe en otra categoría")
                return
            if not cantidad_libro.isdigit() or int(cantidad_libro) == 0:
                messagebox.showerror("Error", "La cantidad debe ser un número mayor que 0")
                return
            libros_info.append((nombre_libro, cantidad_libro))

        # Agregar la nueva categoría
        categorias_libros[nombre_categoria] = libros_info
        messagebox.showinfo("Éxito", "Categoría agregada con éxito")

        # Limpiar los campos
        entry_nombre_categoria.delete(0, tk.END)
        for i in range(5):
            entry_libros[i].delete(0, tk.END)
            entry_cantidad[i].delete(0, tk.END)

    for widget in frame.winfo_children():
        widget.destroy()

    label_instrucciones = tk.Label(frame, text="Agregar una nueva categoría para la tienda :", font=("Arial", 14))
    label_instrucciones.pack(pady=10)

    tk.Label(frame, text="Nombre de la categoría del producto:", font=("Arial", 12)).pack(anchor="w", padx=20)
    entry_nombre_categoria = tk.Entry(frame, font=("Arial", 12))
    entry_nombre_categoria.pack(fill="x", padx=20, pady=5)

    entry_libros = []
    entry_cantidad = []

    for i in range(5):
        frame_libro = tk.Frame(frame)
        frame_libro.pack(fill="x", padx=20, pady=5)
        
        tk.Label(frame_libro, text=f"Nombre del producto {i+1}:", font=("Arial", 12)).pack(side="left")
        entry_libro = tk.Entry(frame_libro, font=("Arial", 12))
        entry_libro.pack(side="left", padx=5, fill="x", expand=True)
        entry_libros.append(entry_libro)
        
        tk.Label(frame_libro, text="precio:", font=("Arial", 12)).pack(side="left", padx=5)
        entry_cantidad_libro = tk.Entry(frame_libro, font=("Arial", 12), width=5)
        entry_cantidad_libro.pack(side="left")
        entry_cantidad.append(entry_cantidad_libro)

    button_agregar_categoria = tk.Button(frame, text="Agregar listado de productos", font=("Arial", 14), command=on_agregar_click)
    button_agregar_categoria.pack(pady=20)
    