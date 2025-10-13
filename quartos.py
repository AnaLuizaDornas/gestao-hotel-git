quartos = {101: {"status": "disponivel"}, 102: {"status": "disponivel"}}
def verificar_disponibilidade(numero):
    return quartos.get(numero, {}).get("status") == "disponivel"
def ocupar_quarto(numero):
    if verificar_disponibilidade(numero):
        quartos[numero]["status"] = "ocupado"
        print(f"Quarto {numero} ocupado.")
def liberar_quarto(numero):
    if numero in quartos:
        quartos[numero]["status"] = "disponivel"
        print(f"Quarto {numero} liberado.")