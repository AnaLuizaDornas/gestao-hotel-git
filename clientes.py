
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
clientes = []

def registrar_cliente(nome, email):
    cliente = Cliente(nome, email)
    clientes.append(cliente)
    print(f"Cliente {nome} registrado.")