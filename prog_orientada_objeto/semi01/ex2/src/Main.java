public class Main {
    public static void main(String[] args) {
        Veiculo corsa = new Veiculo("Chevrolet", "Corsa", 2006);
        Veiculo uno = new Veiculo("Fiat", "Uno", 2010);

        corsa.ligar();
        corsa.desligar();

        uno.ligar();
        uno.desligar();


    }
}