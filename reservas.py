from clientes import Cliente
from quartos import verificar_disponibilidade, ocupar_quarto
reservas = []
def criar_reserva(cliente, numero_quarto):
    if verificar_disponibilidade(numero_quarto):
        ocupar_quarto(numero_quarto)
        reservas.append({"cliente": cliente, "quarto": numero_quarto})
        print(f"Reserva para {cliente.nome} criada no quarto {numero_quarto}.")