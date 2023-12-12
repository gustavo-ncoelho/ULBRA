import org.w3c.dom.ls.LSOutput;

public class CalculadoraBasica extends Calculadora implements Soma, Subtracao, Divisao, Multiplicacao {

    @Override
    public double divisao(double valor1, double valor2) {
        return valor1 / valor2;
    }

    @Override
    public double multiplicacao(double valor1, double valor2) {
        return valor1 * valor2;
    }

    @Override
    public double subtracao(double valor1, double valor2) {
        return valor1 - valor2;
    }

    @Override
    public double soma(double valor1, double valor2) {
        return valor1 + valor2;
    }

}
