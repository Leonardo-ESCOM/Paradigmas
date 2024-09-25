public class PROGRAMA_3 {
    public static void main(String[] args) {
        int n=0, potencia_de_dos=0;
        int valor_mas_bajo, valor_mas_alto;

        if(n<=1){
            System.out.printf("La potencia más cercana al número que ingreso es : 1");
        }
        else {
        int i;
            for (i = 0; ; i++) {
            potencia_de_dos = (int ) Math.pow(2,i);
                if (potencia_de_dos >= n){
                    valor_mas_bajo = n - (int) Math.pow(2, i - 1);
                    valor_mas_alto = (int) Math.pow(2, i) - n;
                    break;
                }
            }
            potencia_de_dos = (valor_mas_bajo < valor_mas_alto) ? (int )Math.pow(2, i - 1) : (int) Math.pow(2, i);
            System.out.printf("La potencia más cercana al númeor que ingreso es : %d", potencia_de_dos);
        }
    }
}

