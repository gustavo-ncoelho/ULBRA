public class Quadrado extends FiguraGeometrica {
    int lado;
    public double calcularArea(){
        return lado*lado;
    }
    public double calcularPerimetro(){
        return lado+lado+lado+lado;
    }
}
