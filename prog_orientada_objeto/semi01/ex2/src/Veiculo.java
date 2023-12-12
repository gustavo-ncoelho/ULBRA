public class Veiculo {
    public String marca;
    public String modelo;
    public int ano;
    public Veiculo(String marca, String modelo, int ano){
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }
    public void ligar(){
        System.out.println("Carro " + modelo + " ligou!!!");
    }
    public void desligar(){
        System.out.println("Carro " + modelo + " desligou!!!");
    }
}
