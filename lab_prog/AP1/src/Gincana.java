public class Gincana {
    private String nomeGincana;
    private int totalEstudantes;
    private Estudante estudanteVencedor;
    private int pontuacaoMaxima;

    public String getNomeGincana() {
        return nomeGincana;
    }

    public void setNomeGincana(String nomeGincana) {
        this.nomeGincana = nomeGincana;
    }

    public int getTotalEstudantes() {
        return totalEstudantes;
    }

    public void setTotalEstudantes(int totalEstudantes) {
        this.totalEstudantes = totalEstudantes;
    }

    public Estudante getEstudanteVencedor() {
        return estudanteVencedor;
    }

    public void setEstudanteVencedor(Estudante estudanteVencedor) {
        this.estudanteVencedor = estudanteVencedor;
    }

    public int getPontuacaoMaxima() {
        return pontuacaoMaxima;
    }

    public void setPontuacaoMaxima(int pontuacaoMaxima) {
        this.pontuacaoMaxima = pontuacaoMaxima;
    }

    public void adicionarEstudante(Estudante estudante) {
        this.totalEstudantes++;
        if (estudante.getPontos() > this.pontuacaoMaxima) {
            this.estudanteVencedor = estudante;
            this.pontuacaoMaxima = estudante.getPontos();
        }
    }

    public void exibirVencedor() {
        System.out.println("Parabéns " + this.estudanteVencedor.getNome() + ", você foi o(a) vencedor(a)!!!");
        System.out.println("Você marcou " + this.estudanteVencedor.getPontos() + " pontos.");
    }
}