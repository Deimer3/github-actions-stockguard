import pytest
from src.inventario import clasificar_stock, detectar_sobrestock

def test_stock_agotado():
    assert clasificar_stock(0, 20) == "AGOTADO"

def test_stock_critico():
    assert clasificar_stock(7, 20) == "CRITICO"

def test_stock_bajo():
    assert clasificar_stock(15, 20) == "BAJO"

def test_stock_normal():
    assert clasificar_stock(30, 20) == "NORMAL"

def test_stock_invalido():
    with pytest.raises(ValueError):
        clasificar_stock(-2, 20)
# --- Nuevas pruebas para la funcionalidad de sobrestock ---

def test_sobrestock_confirmado():
    # El stock (65) supera el triple del mínimo (20 * 3 = 60)
    assert detectar_sobrestock(65, 20) == "SOBRESTOCK"

def test_sobrestock_normal():
    # El stock (45) es inferior al límite de sobrestock (20 * 3 = 60)
    assert detectar_sobrestock(45, 20) == "NORMAL"

def test_sobrestock_caso_limite():
    # El stock (60) es exactamente el triple. La regla dice "mayor a", así que debe ser NORMAL
    assert detectar_sobrestock(60, 20) == "NORMAL"