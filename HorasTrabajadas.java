import java.util.Scanner;

public class HorasTrabajadas {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);


        System.out.print("Introduce el total de horas trabajadas: ");
        double horasTrabajadas = sc.nextDouble();

        System.out.print("Introduce el sueldo por hora: ");
        double sueldoPorHora = sc.nextDouble();


        double pagoRegular = 0;
        double pagoExtra = 0;
        double pagoTotal = 0;


        if (horasTrabajadas > 40) {
            pagoRegular = 40 * sueldoPorHora;
            double horasExtras = horasTrabajadas - 40;
            pagoExtra = horasExtras * sueldoPorHora * 1.5; // 150% del sueldo base
        } else {
            pagoRegular = horasTrabajadas * sueldoPorHora;
        }


        pagoTotal = pagoRegular + pagoExtra;


        System.out.println("Pago regular por las primeras 40 horas: $" + pagoRegular);
        System.out.println("Pago por horas extra: $" + pagoExtra);
        System.out.println("Pago total: $" + pagoTotal);


        sc.close();
    }
}
