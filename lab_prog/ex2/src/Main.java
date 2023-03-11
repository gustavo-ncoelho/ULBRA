public class Main {
    public static void main(String[] args) {

        // a:
        int i = 10;

        while (i <= 25){
            System.out.println(i);
            i++;
        }

        System.out.println("------------------------");

        // b:

        int y = 1;
        int soma = 0;

        while (y < 100) {
            soma += y;
            y += 2;
        }

        System.out.println("A soma dos números é: " + soma);

        System.out.println("------------------------");

        // c:

        int x = 0;
        int z = 0;

        while (x + z < 100){
            System.out.println(z);
            x += z;
            z++;
        }

        System.out.println("------------------------");

        // d:

        int nove = 9;

        for (int f = 1; f < 10; f++){
            int resultado = f * nove;
            System.out.println(nove + " x " + f + " = " + resultado );
        }

        System.out.println("------------------------");
    }
}