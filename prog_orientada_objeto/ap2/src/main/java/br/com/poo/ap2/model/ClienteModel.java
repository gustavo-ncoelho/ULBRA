package br.com.poo.ap2.model;

public class ClienteModel {
    private int id;
    private String nome;
    private int idade;
    private String profissao;
    public int getId() {
        return id;
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

    public String getProfissao() {
        return profissao;
    }

    public void setProfissao(String profissao) {
        this.profissao = profissao;
    }

    public void setId(int id) {
        this.id = id;
    }
}
