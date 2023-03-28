public class Trapezio {
    int baseMenorTrap;
    int baseMaiorTrap;
    int altTrap;

    double calcularArea(){
        return(((baseMaiorTrap+baseMenorTrap)/2)*altTrap);
    }
}
