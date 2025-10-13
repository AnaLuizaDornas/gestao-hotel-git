quartos = {101: {"status": "disponivel"}, 102: {"status": "disponivel"}}
def verificar_disponibilidade(numero):
    return quartos.get(numero, {}).get("status") == "disponivel"