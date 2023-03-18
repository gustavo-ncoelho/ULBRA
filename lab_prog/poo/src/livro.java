import java.util.Date;

public class livro {

    String ibn;
    int numPaginas;
    String editora;

    void reservar(int dias){
        System.out.println("Dias => " + dias);
    }
    void reservar(Date data){
        System.out.println("Data => " + data);
    }
    void reservar(cliente c, Date data ){
        System.out.println("Nome do cliente: " + c.nome + "Data => " + data);
    }
}
