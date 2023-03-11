class Main {
    public static void main(String[] args) {

        double nota1 = 8.5;
        double nota2 = 7.5;
        double nota3 = 6;

        int peso1 = 3;
        int peso2 = 2;
        int peso3 = 5;

        double somaNotas = nota1 * (peso1) + nota2 * (peso2) + nota3 * (peso3);
        double somaPesos = peso1 + peso2 + peso3;

        double media = somaNotas / somaPesos;

        System.out.println("A média é: " + media);

    }
}