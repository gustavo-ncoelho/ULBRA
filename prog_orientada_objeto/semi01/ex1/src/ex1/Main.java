package ex1;

public class Main {
    public static void main(String[] args) {
        Produto sabonete = new Produto("Dove", 3,"Maciu");
        Produto shampoo = new Produto("Monange",7.50, "Xeroso");
        Produto pastaDeDente = new Produto("Colgate", 15.60, "Refrescante");

        Carrinho carrinhoDoBistek = new Carrinho();

        carrinhoDoBistek.adicionarAoCarrinho(sabonete);
        carrinhoDoBistek.adicionarAoCarrinho(shampoo);
        carrinhoDoBistek.mostrarValorTotal();
        carrinhoDoBistek.adicionarAoCarrinho(pastaDeDente);
        carrinhoDoBistek.mostrarValorTotal();

        carrinhoDoBistek.getListaCarrinho();

        System.out.println(carrinhoDoBistek.getValorTotal());
    }
}