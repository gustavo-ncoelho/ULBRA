abstract class Produto {
    private String titulo;

    public Produto(String titulo) {
        this.titulo = titulo;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setTitulo(String titulo, int numeroEdicao) {
        this.titulo = titulo + " - Edição " + numeroEdicao;
    }

    public abstract String detalhesDoProduto();
}
