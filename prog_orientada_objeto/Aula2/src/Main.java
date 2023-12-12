import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> comidas = criarLista();
        adicionarNaLista(comidas,"pizza");
        adicionarNaLista(comidas,"sushi");
        adicionarNaLista(comidas,"batata frita");
        adicionarNaLista(comidas,"hamburgues");
        adicionarNaLista(comidas,"macarrão");
        lerLista(comidas);
        atualizarLista(comidas, 2,"batatas fritas");
        lerLista(comidas);
        deletarPorIndex(comidas, 4);
        lerLista(comidas);
        deletarPorNome(comidas,"sushi");
        lerLista(comidas);
    }
    public static ArrayList<String> criarLista(){
        return new ArrayList<String>();
    }
    public static void lerLista (ArrayList<String> nomeLista){
        System.out.println(nomeLista);
    }

    public static void adicionarNaLista(ArrayList<String> nomeLista, String elemento){
        nomeLista.add(elemento);
    }

    public static void atualizarLista(ArrayList<String> nomeLista, int posicao, String nomeAtualizado){
        nomeLista.set(posicao,nomeAtualizado);
    }

    public static void deletarPorIndex(ArrayList<String> nomeLista, int posicao){
        nomeLista.remove(posicao);
    }

    public static void deletarPorNome(ArrayList<String> nomeLista, String nomeElemento){
        nomeLista.remove(nomeElemento);
    }
}