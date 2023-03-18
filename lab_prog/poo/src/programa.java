import java.util.Date;

public class programa {

    public static void main(String[] args) {
        livro livro1 = new livro(); //instanciei o objeto
        livro1.ibn = "2222222"; //
        livro1.numPaginas = 395;
        livro1.editora = "Saasdas";
        livro1.reservar(17);
        var data = new Date();
        livro1.reservar(data);

        cliente cliente = new cliente();
        cliente.nome = "Cabelo";
        cliente.endereco = "dasdasda, dasydga 120";

        livro livro2 = new livro();
        livro2.ibn = "dasduashdkas";
        livro2.numPaginas = 2333;
        livro2.editora = "Adasdaf";
    }
}
