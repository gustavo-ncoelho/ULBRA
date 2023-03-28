public class Fracao {
    int numerador;
    int denominador;

    void multiplicarFracao(int num, int denom){
        int novoNumerador = numerador * num;
        int novoDenominador = denominador * denom;
        System.out.println("A nova fração é: " + novoNumerador + "/" + novoDenominador);
    }
}
