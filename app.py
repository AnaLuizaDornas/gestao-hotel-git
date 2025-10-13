from clientes import registrar_cliente, listar_clientes, Cliente
from quartos import listar_quartos
from reservas import criar_reserva, cancelar_reserva, listar_reservas

if __name__ == "__main__":
    while True:
        print("\n1. Registrar Cliente\n2. Listar Clientes\n3. Listar Quartos\n4. Criar Reserva\n5. Cancelar Reserva\n6. Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            registrar_cliente(nome, email)
        elif op == "2":
            listar_clientes()
        elif op == "3":
            listar_quartos()
        elif op == "4":
            nome = input("Nome do cliente: ")
            email = input("Email: ")
            quarto = int(input("Número do quarto: "))
            criar_reserva(Cliente(nome, email), quarto)
        elif op == "5":
            quarto = int(input("Número do quarto: "))
            cancelar_reserva(quarto)
        elif op == "6":
            break