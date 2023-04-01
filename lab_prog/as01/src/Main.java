public class Main {
    public static void main(String[] args) {
        circulo circulo1 = new circulo();
        circulo1.raioCirculo = 3.5;
        System.out.println("A área do circulo é: " + circulo1.calcularAreaCirc());
        System.out.println("O perímetro do circulo é: " + circulo1.calcularPerimetroCirc());

        livro livro1 = new livro();
        livro1.autorLivro = "Gustavo";
        livro1.editoraLivro = "sbd";
        livro1.tituloLivro = "altos livro";
        livro1.qtdPaginasLivro = 560;
        livro1.exibirDetalhes();

        animal animal1 = new animal();
        animal1.especieAnimal = "jabuti";
        animal1.idadeAnimal = 150;
        animal1.nomeAnimal = "roberto";
        animal1.dormir();
        animal1.emitirSom();
    }
}