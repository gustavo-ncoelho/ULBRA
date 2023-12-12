class ContaSalario extends Conta {
    public ContaSalario(int numeroConta, double saldo) {
        super(numeroConta, saldo);
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public boolean sacar(double valor) {
        if (saldo >= valor) {
            saldo -= valor;
            return true;
        }
        return false;
    }

    public boolean transferir(Conta destino, double valor) {
        return false; // ContaSalario não permite transferências
    }
}