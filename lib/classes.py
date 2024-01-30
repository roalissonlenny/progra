class articulo():
    def __init__(self, idArt, marca, nombre, precio=None, peso=None, dcto=None, inv=None):
        self.idArt = idArt
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.dcto = dcto
        self.inv = inv
    pass

    def __str__(self):
        return f"idArt: {self.idArt} - marca: {self.marca} - nombre: {self.nombre} - precio: {self.precio} - peso {self.peso} - dcto: {self.dcto} - inv: {self.inv}"


    def setPrecio(self, price):
        self.precio=price
        return 0




class carritou():
    pass
    
