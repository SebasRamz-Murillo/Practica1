
import json

class JSON_FILE:
    def __init__(self, file_path):
        self.file_path = file_path

    def crear(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)



    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except:
            return []


if __name__ == "__main__":
    json_handler = JSON_FILE('data.json')
    datos = {
        "nombre": "Juan",
        "edad": 30,
        "direccion": "Calle Falsa 123"
    }
    json_handler.crear(datos)
    lectura = json_handler.read()
    print(lectura)
