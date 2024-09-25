import java.util.Scanner; //Clase scanner

public class PROGRAMA_2 {

    public static void main(String[] args) {
        int a = 2, b = 4;


        Cuadrante(a, b); //aSÍ SE LLAMA EN JAVA
    }

    public static void Cuadrante(int a, int b) { // Método que recibe dos parámetros de tipo entero
        if (a == 0 && b == 0) {
            System.out.println("La coordenada se encuentra en el origen");
        } else if (a == 0) {

            if (b > 0) {
                System.out.println("La coordenada se encuentra en el eje positivo de las Y");
            } else {
                System.out.println("La coordenada se encuentra en el eje negativo de las Y");
            }
        } else if (b == 0) {
            // Eje X
            if (a > 0) {
                System.out.println("La coordenada se encuentra en el eje positivo de las X");
            } else {
                System.out.println("La coordenada se encuentra en el eje negativo de las X");
            }
        } else if (a > 0 && b > 0) {
            System.out.println("La coordenada se encuentra en el primer cuadrante");
        } else if (a < 0 && b > 0) {
            System.out.println("La coordenada se encuentra en el segundo cuadrante");
        } else if (a < 0 && b < 0) {
            System.out.println("La coordenada se encuentra en el tercer cuadrante");
        } else if (a > 0 && b < 0) {
            System.out.println("La coordenada se encuentra en el cuarto cuadrante");
        }
    }
}
