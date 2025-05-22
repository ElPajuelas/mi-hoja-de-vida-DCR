from Peliculap import Pelicula

def main():
    # Crear 3 nuevas instancias de la clase Pelicula
    peli1 = Pelicula(6, "Interstellar", 169, "Christopher Nolan", False)
    peli2 = Pelicula(7, "Parasite", 132, "Bong Joon-ho", False)
    peli3 = Pelicula(8, "Coco", 105, "Lee Unkrich", True)

    # Mostrar información de cada película
    print(peli1)
    print(peli2)
    print(peli3)

    # Usar métodos de instancia
    print(peli1.prestar())
    print(peli2.prestar())
    print(peli3.devolver())

    # Mostrar el costo de cada película con un precio por minuto
    print(peli1.metodo_de_construcion(20))
    print(peli2.metodo_de_construcion(15))
    print(peli3.metodo_de_construcion(10))

if __name__ == "__main__":
    main()
