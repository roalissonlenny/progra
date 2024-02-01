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

    def setpeso(self, peso):
        self.peso=peso
        return 0

    def setdcto(self, dcto):
        self.dcto=dcto 
        return 0

    def setinv(self, inv):
        self.inv=inv
        return 0

    def getpricedcto(self):
        if self.dcto != None:
            preciodcto= self.precio - (self.precio * (self.dcto/100))
        else:
            preciodcto= self.precio
        return preciodcto


class carritou():
    def __init__(self, idCart):
        self.idCart = idCart
        self.articulos = []
        pass

    def __str__(self):
        printcarrito = f'Csrrito numero: {self.idCart}'
        for i in range(0, len(self.articulos), 1):
            printcarrito += f"articulos: {self.articulos[i]}"
        
        return printcarrito

    def addarticulo(self, idArt):
        self.articulos.append( idArt )
        return 0



    pass
    
