
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
clientes = []
def saudacao():
    print("Olá, cliente! Seja bem-vindo!")

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

if __name__ == "__main__":
    registrar_cliente("Ana Luiza", "ana@example.com")
    listar_clientes()
    