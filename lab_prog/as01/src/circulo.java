public class circulo {
    double raioCirculo;
    double calcularPerimetroCirc(){
        return(Math.PI * raioCirculo * 2);
    }
    double calcularAreaCirc(){
        return(Math.PI * (Math.pow(raioCirculo, 2)));
    }

}
