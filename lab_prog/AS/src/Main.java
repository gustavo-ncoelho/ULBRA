public class Main {
    public static void main(String[] args) {

        Animal animal1 = new Animal("Animal1",5,145,"Esperie1");
        animal1.movimentar("Restajante");

        Mamifero mamifero1 = new Mamifero("Mamifero1", 5, 15.2, "Espécie2", "Pelagem1");
        mamifero1.amamentar();

        Ave ave1 = new Ave("Ave1", 2, 1.5, "Espécie3", 0.8);
        ave1.voar();
        ave1.realizarTruque();

        Veterinario veterinario1 = new Veterinario("Veterinario1", "Cargo1", 5000.0, "Especialidade1");
        veterinario1.realizarExame(mamifero1);

        Zoo zoo = new Zoo(10, 5);
        zoo.adicionarAnimal(ave1);
        zoo.adicionarAnimal(mamifero1);
        zoo.adicionarFuncionario(veterinario1);

        // Exemplo de uso dos métodos get e set
        System.out.println("Nome do animal: " + ave1.getNome());
        ave1.setNome("Ave99");
        System.out.println("Novo nome do animal: " + ave1.getNome());

        System.out.println("Nome do animal: " + mamifero1.getNome());
        mamifero1.setNome("Mamifero99");
        System.out.println("Novo nome do animal: " + mamifero1.getNome());
    }
}