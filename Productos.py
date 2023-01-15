from Lista import Lista


class Producto(Lista):
    def __init__(self, codigo="", nombre="", descripcion="", precio=""):
        super().__init__("productos.json")
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def to_dict(self):
        return {"codigo": self.codigo, "nombre": self.nombre, "descripcion": self.descripcion,
                "precio": self.precio}

if __name__ == "__main__":
    # productos = Lista("productos.json")
    # producto1 = Producto("75011", "Xbox", "consola", 30000)
    # producto2 = Producto("75012", "Play", "consola", 49000)
    # producto3 = Producto("75013", "Wii", "consola", 2000)
    # productos.crear(producto1)
    # productos.crear(producto2)
    # productos.crear(producto3)
    # print(productos.buscar_parametro('nombre','Wii'))
    producto = Producto()
    producto_Xbox = producto.buscar_parametro("nombre", "Xbox")
    print(producto_Xbox)
