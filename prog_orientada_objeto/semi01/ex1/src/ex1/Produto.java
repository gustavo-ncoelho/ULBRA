package ex1;

public class Produto {
    private String nomeProduto;
    private double valorProduto;
    private String descricaoProduto;

    public Produto(String nomeProduto, double valorProduto, String descricaoProduto){
        this.nomeProduto = nomeProduto;
        this.valorProduto = valorProduto;
        this.descricaoProduto = descricaoProduto;
    }

    public String getNomeProduto() {
        return nomeProduto;
    }

    public void setNomeProduto(String nomeProduto) {
        this.nomeProduto = nomeProduto;
    }

    public double getValorProduto() {
        return valorProduto;
    }

    public void setValorProduto(double valorProduto) {
        this.valorProduto = valorProduto;
    }

    public String getDescricaoProduto() {
        return descricaoProduto;
    }

    public void setDescricaoProduto(String descricaoProduto) {
        this.descricaoProduto = descricaoProduto;
    }
}
