import codecs
# clase Persona
class Persona(object):
    #constructor de la clase
    def __init__(self, nom, apell, edad):
        self.nombre = nom
        self.apellido = apell
        self.edad = int(edad)


#metodos get and set
    def agrgarNombre(self, n):
        self.nombre = n

    def obtenerNombre(self):
        return self.nombre

    def agregarApellido(self, a):
        self.apellido = a

    def obtenerApellido(self):
        return self.apellido

    def agregarEdad(self, e):
        self.edad = int(e)

    def obtenerEdad(self):
        return self.edad

#Sobreescritura del metodo toString
    def __str__(self):
        """
        """
        return "%s  %s %d" % (self.nombre, self.apellido, self.edad)

#clase LeerArchivo
class LeerArchivo(object):
    def __init__(self):
        self.archivo = codecs.open("ejemplo.txt", "r")  # abre el rchivo

    # metodo para obtener la informacion que se encuentra en el archivo
    def obtener_informacion(self):
        return self.archivo.readlines()
    # metodo para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()
