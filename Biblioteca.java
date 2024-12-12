import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Biblioteca {
    private Scanner scanner = new Scanner(System.in); // Declaración única del scanner
    List<Libro> listaLibros = new ArrayList<>(); // Inicialización de la lista

    public void inicializar() {
        boolean continuar = true;

        while (continuar) {
            System.out.println("Bienvenido a la Biblioteca, selecciona una opción:");
            System.out.println("1. Visualizar colección\n2. Añadir libro a la biblioteca");
            System.out.println("3. Buscar libro en base a Identificador\n4. Prestar libro\n5. Devolver libro");
            System.out.println("6. Salir del programa");

            int opcion = scanner.nextInt();
            scanner.nextLine(); // Limpia el búfer

            switch (opcion) {
                case 1:
                    visualizarColeccion();
                    break;

                case 2:
                    AnadirLibro();
                    break;

                case 3:
                    BuscarLibro();
                    break;

                case 4:
                    PrestarLibro();
                    break;

                case 5:
                    DevolverLibro();
                    break;

                case 6:
                    continuar = false;
                    System.out.println("Saliendo del programa...");
                    break;

                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
            }
        }
    }

    public void visualizarColeccion() {
        if (listaLibros.isEmpty()) {
            System.out.println("La colección está vacía. No hay libros para mostrar.");
            return;
        }

        System.out.println("Colección de libros:");
        for (int i = 0; i < listaLibros.size(); i++) {
            System.out.println((i + 1) + ". " + listaLibros.get(i));
        }
        System.out.println("\n");
    }

    public void AnadirLibro() {
        System.out.println("¿Cuántos libros desea agregar?");
        int cantidad = scanner.nextInt();
        scanner.nextLine(); // Limpia el búfer

        for (int i = 0; i < cantidad; i++) {
            System.out.println("Por favor, ingresa los datos del libro:");

            System.out.print("Título: ");
            String titulo = scanner.nextLine();

            System.out.print("Autor: ");
            String autor = scanner.nextLine();

            System.out.print("ISBN: ");
            String isbn = scanner.nextLine();

            listaLibros.add(new Libro(titulo, autor, isbn));
            System.out.println("Libro agregado exitosamente.");
        }
    }

    public void BuscarLibro() {
        System.out.println("Por favor, ingresa el ISBN del libro:");
        String isbn = scanner.nextLine();

        for (Libro libro : listaLibros) {
            if (libro.getIsbn().equals(isbn)) {
                System.out.println("Libro encontrado: " + libro + "\n");
                return;
            }
        }

        System.out.println("No se encontró el libro.");
    }

    public void PrestarLibro() {
        System.out.println("Por favor, ingresa el ISBN del libro:");
        String isbn = scanner.nextLine();

        for (Libro libro : listaLibros) {
            if (libro.getIsbn().equals(isbn)) {
                if (libro.getEstado().equals("devuelto")) {
                    libro.setEstado("prestado");
                    System.out.println("El libro se prestó exitosamente.\n");
                } else {
                    System.out.println("El libro ya está prestado.\n");
                }
                return;
            }
        }

        System.out.println("No se encontró el libro.\n");
    }

    public void DevolverLibro() {
        System.out.println("Por favor, ingresa el ISBN del libro:");
        String isbn = scanner.nextLine();

        for (Libro libro : listaLibros) {
            if (libro.getIsbn().equals(isbn)) {
                if (libro.getEstado().equals("devuelto")) {
                    System.out.println("El libro ya está devuelto.\n");
                } else if (libro.getEstado().equals("prestado")) {
                    libro.setEstado("devuelto");
                    System.out.println("El libro se devolvió exitosamente.\n");
                }
                return;
            }
        }

        System.out.println("No se encontró el libro.\n");
    }
}
