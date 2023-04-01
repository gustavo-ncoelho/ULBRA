public class livro {
    String tituloLivro;
    String autorLivro;
    String editoraLivro;
    int qtdPaginasLivro;
    void exibirDetalhes(){
        System.out.println("O título do livro é: " + tituloLivro);
        System.out.println("O autor do livro é: " + autorLivro);
        System.out.println("A editora do livro é: " + editoraLivro);
        System.out.println("O livro tem " + qtdPaginasLivro + " páginas");
    }
}
