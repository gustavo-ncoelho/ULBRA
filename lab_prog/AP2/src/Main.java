public class Main {
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();

        Livro livro1 = new Livro("@@@@@@@@@@", "Autor 1", 2020, true);
        Livro livro2 = new Livro("##########", "Autor 2", 2018, false);
        Livro livro3 = new Livro("%%%%%%%%%%", "Autor 3", 2019, true);
        Livro livro4 = new Livro("!!!!!!!!!!", "Autor 4", 2017, true);
        Livro livro5 = new Livro("$$$$$$$$$$", "Autor 5", 2021, false);

        livro5.setTitulo("$$$$$$$$$$", 2);
        System.out.println(livro5);

        biblioteca.adicionarLivro(livro1);
        biblioteca.adicionarLivro(livro2);
        biblioteca.adicionarLivro(livro3);
        biblioteca.adicionarLivro(livro4);
        biblioteca.adicionarLivro(livro5);

        biblioteca.listarLivros();

        biblioteca.removerLivro("##########");

        biblioteca.atualizarDetalhesLivro("!!!!!!!!!!", "Autor 4", 2017, false);

        biblioteca.verificarDisponibilidadeLivro("%%%%%%%%%%");
        biblioteca.verificarDisponibilidadeLivro("!!!!!!!!!!");


    }
}