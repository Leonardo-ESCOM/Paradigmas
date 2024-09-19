public class Main {
    public static void main(String[] args) { // Porque en el método tengo que ponerle string args ?
        int a=25,b=6;
        int P_triangulo, P_cuadrado, A_cuadrado, P_rectangulo, A_rectangulo ;

        P_triangulo = 6+6+6;
        P_cuadrado = 4*b;
        A_cuadrado = b*b;
        P_rectangulo = 2*a + 2*b;
        A_rectangulo = a*b;



        System.out.printf("El Perímetro de un triangulo de lado " + b +" es: " + P_triangulo);
        System.out.printf("%nEl Perímetro de un cuadrado de lado " + b + " es: " + P_cuadrado);
        System.out.printf("%nEl Area de un cuadrado de lado " + b + " es: " + A_cuadrado);
        System.out.printf("%nEl Perímetro de un rectangulo de lados" + a + " y lado " + b + " es: " + P_rectangulo);
        System.out.printf("%nEl Área de un rectangulo de ladoa"  + a + " y lado " + b + " es: " + A_rectangulo);



        }
    }