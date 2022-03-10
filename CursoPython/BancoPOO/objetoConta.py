from conta import Conta, ContaCorrente, ContaPoupanca
from cliente import Cliente

objeto_conta = Conta(123, 456, 182)
print(objeto_conta.depositar(50))

cliente1 = Cliente('Luiz', 30)

conta1 = ContaPoupanca(1111, 254136, 0)

cliente1.inserir_conta(conta1)

cliente1.conta.depositar(60)
cliente1.conta.sacar(62)


