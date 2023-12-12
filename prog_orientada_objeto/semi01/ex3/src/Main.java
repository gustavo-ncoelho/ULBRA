public class Main {
    public static void main(String[] args) {
        ContaCorrente contaCorrente = new ContaCorrente(1, 1000, 500);
        ContaPoupanca contaPoupanca = new ContaPoupanca(2, 5000);
        ContaSalario contaSalario = new ContaSalario(3, 2000);

        System.out.println("Saldo Conta Corrente: " + contaCorrente.consultarSaldo());
        System.out.println("Saldo Conta Poupança: " + contaPoupanca.consultarSaldo());
        System.out.println("Saldo Conta Salário: " + contaSalario.consultarSaldo());

        contaCorrente.depositar(300);
        contaPoupanca.sacar(700);
        contaCorrente.transferir(contaPoupanca, 200);

        System.out.println("Saldo Conta Corrente: " + contaCorrente.consultarSaldo());
        System.out.println("Saldo Conta Poupança: " + contaPoupanca.consultarSaldo());
    }
}