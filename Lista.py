from JSON import  JSON_FILE as JSON

class Lista:
    def __init__(self, archivo):
        self.json = JSON(archivo)
        self.listas = self.json.read()

    def crear(self, item):
        self.listas.append(item)
        self.json.crear(self.listas)

    def mostrar(self):
        return self.listas

    def actualizar(self, index, item):
        self.listas[index] = item
        self.json.crear(self.listas)

    def eliminar(self, index):
        del self.listas[index]
        self.json.crear(self.listas)

    def eliminar_todo(self):
        self.listas.clear()
        self.json.crear(self.listas)

    def buscar_parametro(self, llave, valor):
        for item in self.listas:
            if item[llave] == valor:
                return item
        return None


