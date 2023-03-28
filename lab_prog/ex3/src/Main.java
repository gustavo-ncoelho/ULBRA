public class Main {
    public static void main(String[] args) {
        Quadrado quadrado1 = new Quadrado();
        quadrado1.ladoQuadrado = 4;
        System.out.println("Área do quadrado é: " + quadrado1.calcularArea());

        Trapezio trapezio1 = new Trapezio();
        trapezio1.altTrap = 6;
        trapezio1.baseMenorTrap = 2;
        trapezio1.baseMaiorTrap = 3;
        System.out.println("Área do trapézio é: " + trapezio1.calcularArea());

        Circulo circulo1 = new Circulo();
        circulo1.raioCirculo = 3;
        System.out.println("Área do circulo é: " + circulo1.calcularArea());

        Triangulo triangulo1 = new Triangulo();
        triangulo1.altTriangulo = 5;
        triangulo1.baseTriangulo = 8;
        System.out.println("Área do triângulo é: " + triangulo1.calcularArea());


    }
}