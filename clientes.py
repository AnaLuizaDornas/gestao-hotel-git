
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
clientes = []

def registrar_cliente(nome, email):
    cliente = Cliente(nome, email)
    clientes.append(cliente)
    print(f"Cliente {nome} registrado.")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente registrado.")
    else:
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente.nome} - {cliente.email}")