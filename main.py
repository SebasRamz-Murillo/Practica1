from Productos import Producto
from Clientes import Cliente
from Ventas import Venta

import tkinter as tk

root = tk.Tk()
root.title("Simple Window")
root.geometry("600x400")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()
