abstract class Conta {
    protected int numeroConta;
    protected double saldo;

    public Conta(int numeroConta, double saldo) {
        this.numeroConta = numeroConta;
        this.saldo = saldo;
    }

    public abstract void depositar(double valor);
    public abstract boolean sacar(double valor);
    public abstract boolean transferir(Conta destino, double valor);
    public double consultarSaldo() {
        return saldo;
    }
}