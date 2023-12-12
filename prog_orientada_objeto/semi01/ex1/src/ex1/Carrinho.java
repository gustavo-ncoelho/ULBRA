package ex1;

import java.util.ArrayList;
import java.util.List;
public class Carrinho {
    private ArrayList<Produto> listaCarrinho;
    private double valorTotal;
    public Carrinho(){
        listaCarrinho = new ArrayList<>();
    }
    public void adicionarAoCarrinho(Produto produto){
        listaCarrinho.add(produto);
        System.out.println(produto.getNomeProduto() + " adicionado ao carrinho");
        valorTotal += produto.getValorProduto();
    }

    public void mostrarValorTotal(){
        System.out.println("O valor total é de: R$" + valorTotal);
    }

    public List<Produto> getListaCarrinho() {
        return listaCarrinho;
    }

    public double getValorTotal() {
        return valorTotal;
    }
}
