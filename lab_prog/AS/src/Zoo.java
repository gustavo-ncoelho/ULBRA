public class Zoo {
    private Animal[] animais;
    private Funcionario[] funcionarios;
    private int numAnimais;
    private int numFuncionarios;

    public Zoo(int capacidadeAnimais, int capacidadeFuncionarios) {
        animais = new Animal[capacidadeAnimais];
        funcionarios = new Funcionario[capacidadeFuncionarios];
        numAnimais = 0;
        numFuncionarios = 0;
    }

    public void adicionarAnimal(Animal animal) {
        if (numAnimais < animais.length) {
            animais[numAnimais] = animal;
            numAnimais++;
            System.out.println("Animal adicionado com sucesso.");
        } else {
            System.out.println("Capacidade máxima de animais atingida.");
        }
    }

    public void adicionarFuncionario(Funcionario funcionario) {
        if (numFuncionarios < funcionarios.length) {
            funcionarios[numFuncionarios] = funcionario;
            numFuncionarios++;
            System.out.println("Funcionário adicionado com sucesso.");
        } else {
            System.out.println("Capacidade máxima de funcionários atingida.");
        }
    }
}
