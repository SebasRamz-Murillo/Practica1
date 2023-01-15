from Lista import Lista
from Productos import Producto
from Clientes import Cliente


class Venta(Lista):
    def __init__(self, cliente="", detalle_productos=[], fecha="", total=""):
        super().__init__("ventas.json")
        self.cliente = cliente
        self.detalle_productos = detalle_productos
        self.fecha = fecha
        self.total = total

    def to_dict(self):
        return {"cliente": self.cliente, "detalle_productos": self.detalle_productos, "fecha": self.fecha,
                "total": self.total}


if __name__ == "__main__":
    venta = Venta()
    # producto = Producto()
    # cliente = Cliente()
    # cliente1 = cliente.buscar_parametro("nombre", "Sebas")
    # prod1 = producto.buscar_parametro("nombre", "Xbox")
    # if cliente1 and prod1:
    #     venta = Venta(cliente1, prod1)
    #     venta_dict = venta.to_dict()
    #     venta.crear(venta_dict)
    #     print(venta_dict)
    # else:
    #     print("cliente or producto no encontrado")
