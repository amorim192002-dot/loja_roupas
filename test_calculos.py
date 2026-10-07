import pytest
from .loja.calculos import total_carrinho

def test_soma_preco_vezes_quantidades():

    itens = [(39.90, 3), (129.90, 1)]

    total = total_carrinho(itens)

    assert total == pytest.approx(249.90)

def test_carrinho_vazio_custa_zero():
    assert total_carrinho([]) == 0

def test_soma_preco_vezes_quantidade():
    itens = [(39.90, 3), (129.90, 1)]
    total = total_carrinho(itens)

    assert total == pytest.approx(249.60)