from Lista import Lista


class Cliente(Lista):

    def __init__(self, rfc="", nombre="", telefono=""):
        super().__init__("clientes.json")
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono

    def to_dict(self):
        return {"rfc": self.rfc, "nombre": self.nombre, "telefono": self.telefono}


if __name__ == "__main__":
    cliente = Cliente()
    producto_Xbox = cliente.buscar_parametro("nombre", "Sebas")
    print(producto_Xbox)
