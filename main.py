from lib import *

art1=articulo(10256,"Coca-cola","Canada Dry")
art1.setPrecio(25.00)
art1.setpeso(350)
art1.setdcto(10)
art1.setinv(10)
#print(art1)

cart1=carritou("ABC123")
print(cart1)

cart2=carritou("DEF456")
print(cart2)

cart3=carritou("GHI789")
print(cart3)

art2=articulo(12346,"Bimbo","Pan blanco")
art2.setPrecio(30.00)
art2.setpeso(60)
art2.setinv(15)
#print(art2)

art3=articulo(13590,"Barcel","Rufles")
art3.setPrecio(27.00)
art3.setpeso(25)
art3.setdcto(14)
art3.setinv(35)
#print(art3)

cart1.addarticulo(art1.idArt)
cart1.addarticulo(art2.idArt)
cart1.addarticulo(art3.idArt)

print(cart1)

print(cart2)

