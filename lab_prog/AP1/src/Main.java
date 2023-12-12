public class Main {
    public static void main(String[] args) {
        Gincana gincana = new Gincana();
        gincana.setNomeGincana("Gincana Universitária");
        gincana.setTotalEstudantes(0);
        gincana.setPontuacaoMaxima(0);

        Estudante estudante1 = new Estudante();
        estudante1.setNome("Fabrício");
        estudante1.setIdade(23);
        estudante1.setPontos(104);
        gincana.adicionarEstudante(estudante1);

        Estudante estudante2 = new Estudante();
        estudante2.setNome("José Maria");
        estudante2.setIdade(36);
        estudante2.setPontos(163);
        gincana.adicionarEstudante(estudante2);

        Estudante estudante3 = new Estudante();
        estudante3.setNome("Maria José");
        estudante3.setIdade(26);
        estudante3.setPontos(125);
        gincana.adicionarEstudante(estudante3);

        gincana.exibirVencedor();
    }
}