class Pelicula:
    def __init__(self, codigo=0,titulo="", duracion=0, director="", prestado=False):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__duracion = duracion
        self.__director = director
        self.__prestado = prestado

    def get_codigo(self):
        return self.__codigo
    
    def get_titulo(self):
        return self.__titulo
    def get_duracion(self):
        return self.__duracion
    def get_director(self):
        return self.__director
    def get_prestado(self):
        return self.__prestado
    

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def sety_director(self, director):
        self.__director = director
    def set_prestado(self, prestado):
        self.__prestado = prestado

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            return f"Película {self.__titulo} se presto con exito"
        else:
            return f"Película {self.__titulo} ya se encuentra"
        
    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            return f"Película {self.__titulo} se devolvio a tiempo"
        else:
            return f"Pelicula {self.__titulo} ya habia sido devuelto anteriormente"
        
    def metodo_de_construcion(self, precio_minuto):
        costo= precio_minuto * self.__duracion
        return f"La pelicula {self.__titulo} con una duracion de {self.__duracion} con un precio por minuto de {precio_minuto} cop. Con un total de {costo} cop."

    def __str__(self):
        return f"Codigo: {self.__codigo}, Titulo: {self.__titulo}, Duracion: {self.__duracion}, Director: {self.__director}, Prestado: {self.__prestado}"
    
    def __eq__(self, other):
        if isinstance(other, Pelicula):
            return self.__codigo == other.__codigo
        return False
    

if __name__ == "__main__":
    Pelicula1 = Pelicula(1, "El Padrino", 175, "Francis Ford Coppola", False)
    Pelicula2 = Pelicula(2, "El Señor de los Anillos", 178, "Peter Jackson", True)
    Pelicula3 = Pelicula(3, "Inception", 148, "Christopher Nolan", False)
    Pelicula4 = Pelicula(4, "The Dark Knight", 152, "Christopher Nolan", True)
    Pelicula5 = Pelicula(1, "Pulp Fiction", 154, "Quentin Tarantino", False)

    print(Pelicula1.prestar())
    print(Pelicula1.devolver())
    print(Pelicula1.devolver())

    print(Pelicula1.metodo_de_construcion(20))
    print(Pelicula2.metodo_de_construcion(10))

    print(Pelicula1)
    print(Pelicula2)
    print(Pelicula3)
    print(Pelicula4)
    print(Pelicula5)

    print(Pelicula1 == Pelicula2)
    print(Pelicula1 == Pelicula5)