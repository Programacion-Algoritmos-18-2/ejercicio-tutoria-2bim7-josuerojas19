#importacion de clases
from modelado import *
from combinacion import *
m = LeerArchivo() #declaracion de objeto
lista = m.obtener_informacion()
lista = [l.split(";") for l in lista]
nlista = []
elista = []
for d in lista:
    p = Persona(d[0], d[1], d[2])
    print(p)
    nlista.append(p)
    elista.append(p.edad)
#declaracion de objeto
result = merge_sort(elista)
print(result)