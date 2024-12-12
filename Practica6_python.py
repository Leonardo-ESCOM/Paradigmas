class Libro:
    def __init__(self, titulo, autor, isbn, estado="disponible"):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = estado

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            return True
        return False

    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            return True
        return False

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {self.estado}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        cantidad = int(input("¿Cuántos libros desea agregar? "))
        for _ in range(cantidad):
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            nuevo_libro = Libro(titulo, autor, isbn)
            self.libros.append(nuevo_libro)
            print("Libro agregado exitosamente.")

    def visualizar_coleccion(self):
        if not self.libros:
            print("La colección está vacía.")
        else:
            print("Colección de libros:")
            for i, libro in enumerate(self.libros, start=1):
                print(f"{i}. {libro}")

    def buscar_libro(self):
        isbn = input("Ingrese el ISBN del libro que busca: ")
        for libro in self.libros:
            if libro.isbn == isbn:
                print("Libro encontrado:")
                print(libro)
                return libro
        print("No se encontró el libro.")
        return None

    def prestar_libro(self):
        libro = self.buscar_libro()
        if libro:
            if libro.prestar():
                print("El libro ha sido prestado exitosamente.")
            else:
                print("El libro ya está prestado.")

    def devolver_libro(self):
        libro = self.buscar_libro()
        if libro:
            if libro.devolver():
                print("El libro ha sido devuelto exitosamente.")
            else:
                print("El libro no está prestado.")

    def menu(self):
        while True:
            print("\nMenú de la biblioteca:")
            print("1. Visualizar colección")
            print("2. Agregar libro")
            print("3. Buscar libro")
            print("4. Prestar libro")
            print("5. Devolver libro")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.visualizar_coleccion()
            elif opcion == "2":
                self.agregar_libro()
            elif opcion == "3":
                self.buscar_libro()
            elif opcion == "4":
                self.prestar_libro()
            elif opcion == "5":
                self.devolver_libro()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")



if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu()
