class Biblioteca {
    private Livro livro1;
    private Livro livro2;
    private Livro livro3;
    private Livro livro4;
    private Livro livro5;

    public Biblioteca() {
        this.livro1 = null;
        this.livro2 = null;
        this.livro3 = null;
        this.livro4 = null;
        this.livro5 = null;
    }

    public void adicionarLivro(Livro livro) {
        if (livro1 == null) {
            livro1 = livro;
            System.out.println("Livro adicionado à biblioteca.");
        } else if (livro2 == null) {
            livro2 = livro;
            System.out.println("Livro adicionado à biblioteca.");
        } else if (livro3 == null) {
            livro3 = livro;
            System.out.println("Livro adicionado à biblioteca.");
        } else if (livro4 == null) {
            livro4 = livro;
            System.out.println("Livro adicionado à biblioteca.");
        } else if (livro5 == null) {
            livro5 = livro;
            System.out.println("Livro adicionado à biblioteca.");
        } else {
            System.out.println("Não é possível adicionar o livro. A biblioteca está cheia.");
        }
    }

    public void removerLivro(String titulo) {
        if (livro1 != null && livro1.getTitulo().equalsIgnoreCase(titulo)) {
            livro1 = null;
            System.out.println("Livro removido da biblioteca.");
        } else if (livro2 != null && livro2.getTitulo().equalsIgnoreCase(titulo)) {
            livro2 = null;
            System.out.println("Livro removido da biblioteca.");
        } else if (livro3 != null && livro3.getTitulo().equalsIgnoreCase(titulo)) {
            livro3 = null;
            System.out.println("Livro removido da biblioteca.");
        } else if (livro4 != null && livro4.getTitulo().equalsIgnoreCase(titulo)) {
            livro4 = null;
            System.out.println("Livro removido da biblioteca.");
        } else if (livro5 != null && livro5.getTitulo().equalsIgnoreCase(titulo)) {
            livro5 = null;
            System.out.println("Livro removido da biblioteca.");
        } else {
            System.out.println("Livro não encontrado na biblioteca.");
        }
    }

    public void atualizarDetalhesLivro(String titulo, String autor, int anoPublicacao, boolean disponibilidade) {
        if (livro1 != null && livro1.getTitulo().equalsIgnoreCase(titulo)) {
            livro1.setAutor(autor);
            livro1.setAnoPublicacao(anoPublicacao);
            livro1.setDisponibilidade(disponibilidade);
            System.out.println("Detalhes do livro atualizados.");
        } else if (livro2 != null && livro2.getTitulo().equalsIgnoreCase(titulo)) {
            livro2.setAutor(autor);
            livro2.setAnoPublicacao(anoPublicacao);
            livro2.setDisponibilidade(disponibilidade);
            System.out.println("Detalhes do livro atualizados.");
        } else if (livro3 != null && livro3.getTitulo().equalsIgnoreCase(titulo)) {
            livro3.setAutor(autor);
            livro3.setAnoPublicacao(anoPublicacao);
            livro3.setDisponibilidade(disponibilidade);
            System.out.println("Detalhes do livro atualizados.");
        } else if (livro4 != null && livro4.getTitulo().equalsIgnoreCase(titulo)) {
            livro4.setAutor(autor);
            livro4.setAnoPublicacao(anoPublicacao);
            livro4.setDisponibilidade(disponibilidade);
            System.out.println("Detalhes do livro atualizados.");
        } else if (livro5 != null && livro5.getTitulo().equalsIgnoreCase(titulo)) {
            livro5.setAutor(autor);
            livro5.setAnoPublicacao(anoPublicacao);
            livro5.setDisponibilidade(disponibilidade);
            System.out.println("Detalhes do livro atualizados.");
        } else {
            System.out.println("Livro não encontrado na biblioteca.");
        }
    }

    public void verificarDisponibilidadeLivro(String titulo) {
        if (livro1 != null && livro1.getTitulo().equalsIgnoreCase(titulo)) {
            if (livro1.isDisponivel()) {
                System.out.println("O livro '" + titulo + "' está disponível.");
            } else {
                System.out.println("O livro '" + titulo + "' não está disponível.");
            }
        } else if (livro2 != null && livro2.getTitulo().equalsIgnoreCase(titulo)) {
            if (livro2.isDisponivel()) {
                System.out.println("O livro '" + titulo + "' está disponível.");
            } else {
                System.out.println("O livro '" + titulo + "' não está disponível.");
            }
        } else if (livro3 != null && livro3.getTitulo().equalsIgnoreCase(titulo)) {
            if (livro3.isDisponivel()) {
                System.out.println("O livro '" + titulo + "' está disponível.");
            } else {
                System.out.println("O livro '" + titulo + "' não está disponível.");
            }
        } else if (livro4 != null && livro4.getTitulo().equalsIgnoreCase(titulo)) {
            if (livro4.isDisponivel()) {
                System.out.println("O livro '" + titulo + "' está disponível.");
            } else {
                System.out.println("O livro '" + titulo + "' não está disponível.");
            }
        } else if (livro5 != null && livro5.getTitulo().equalsIgnoreCase(titulo)) {
            if (livro5.isDisponivel()) {
                System.out.println("O livro '" + titulo + "' está disponível.");
            } else {
                System.out.println("O livro '" + titulo + "' não está disponível.");
            }
        } else {
            System.out.println("Livro não encontrado na biblioteca.");
        }
    }

    public void listarLivros() {
        if (livro1 != null) {
            System.out.println(livro1.detalhesDoProduto());
        }
        if (livro2 != null) {
            System.out.println(livro2.detalhesDoProduto());
        }
        if (livro3 != null) {
            System.out.println(livro3.detalhesDoProduto());
        }
        if (livro4 != null) {
            System.out.println(livro4.detalhesDoProduto());
        }
        if (livro5 != null) {
            System.out.println(livro5.detalhesDoProduto());
        }
    }
}