public class Libro {
    // Los atributos tienen un acceso privado para que exista el encapsualmiento
    private String Titulo;
    private String Autor;
    private String isbn;    // Código único del libro
    private String Estado;  // Indica si el libro está "disponible" o "prestado"

    
    //Constructor 
    public Libro (String titulo, String autor, String isbn) {
        this.Titulo = titulo;
        this.Autor = autor;
        this.isbn = isbn;   //Se puede hacer que este valor no pueda ser tipo null?
        this.Estado = "devuelto";
    }

    //Que es override?
    @Override
    public String toString() {
        return "Título: " + Titulo + ", Autor: " + Autor + ", ISBN: " + isbn + ", Estado: " + Estado;
    }


    // get es el método para acceder a los atributos del método cuando son privados
    public String getTitulo()   {    return Titulo;    }

    // set es el método para modificar los atributos del método cuando son privados
    public void setTitulo(String titulo) {
        this.Titulo = titulo;
    }

    public String getAutor()    {    return Autor;    }
    public void setAutor(String autor)  {    this.Autor = autor;    }

    public String getIsbn()     {    return isbn;    }
    public void setIsbn(String isbn) {    this.isbn = isbn;    }

    public String getEstado()   {    return Estado;    }
    public void setEstado(String estado) {    this.Estado = estado;    }

}



