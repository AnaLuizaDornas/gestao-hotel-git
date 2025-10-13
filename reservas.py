from clientes import Cliente
from quartos import verificar_disponibilidade, ocupar_quarto
reservas = []

def criar_reserva(cliente, numero_quarto):
    if verificar_disponibilidade(numero_quarto):
        ocupar_quarto(numero_quarto)
        reservas.append({"cliente": cliente, "quarto": numero_quarto})
        print(f"Reserva para {cliente.nome} criada no quarto {numero_quarto}.")
    else:
        print("Quarto ocupado")

from quartos import liberar_quarto
def cancelar_reserva(numero_quarto):
    for reserva in reservas[:]:
        if reserva["quarto"] == numero_quarto:
            liberar_quarto(numero_quarto)
            reservas.remove(reserva)
            print(f"Reserva no quarto {numero_quarto} cancelada.")
            return

def listar_reservas():
    for reserva in reservas:
        print(f"Cliente: {reserva['cliente'].nome}, Quarto: {reserva['quarto']}")

if __name__ == "__main__":
    c = Cliente("Ana", "ana@example.com")
    criar_reserva(c, 101)  
    criar_reserva(c, 101)  