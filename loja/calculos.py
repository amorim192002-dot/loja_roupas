FRETE_FIXO = 15.0
FRETE_GRATIS_A_PARTIR_DE = 200.0


def total_carrinho(itens):
    """Recebe uma lista de (preço, quantidade) e devolve o total."""
    total = 0
    for preco, quantidade in itens:
        total = total + preco * quantidade
    return total
