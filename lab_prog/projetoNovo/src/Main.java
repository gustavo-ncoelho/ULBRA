public class Main {
    public static void main(String[] args) {

        Quadrado quadrado1 = new Quadrado();
        quadrado1.lado = 7;
        System.out.println(quadrado1.calcularArea());
        System.out.println(quadrado1.calcularPerimetro());
    }
}