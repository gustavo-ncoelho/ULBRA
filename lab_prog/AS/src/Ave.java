public class Ave extends Animal implements Treinavel {
    private double envergaduraAsa;

    public Ave(String nome, int idade, double peso, String especie, double envergaduraAsa) {
        super(nome, idade, peso, especie);
        this.envergaduraAsa = envergaduraAsa;
    }

    public double getEnvergaduraAsa() {
        return envergaduraAsa;
    }

    public void setEnvergaduraAsa(double envergaduraAsa) {
        this.envergaduraAsa = envergaduraAsa;
    }

    public void voar() {
        System.out.println("A ave está voando.");
    }

    @Override
    public void realizarTruque() {
        System.out.println("A ave realizou um truque voador.");
    }
}