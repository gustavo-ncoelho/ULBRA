import java.util.ArrayList;
public class Cliente {
    String nome;
    int idade;
    ArrayList<Conta> conta = new ArrayList<Conta>();
    public ArrayList<Conta> getConta() {
        return conta;
    }
    public void addConta(ArrayList<Conta> ArrayConta, Conta conta){
        ArrayConta.add(conta);
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

}
