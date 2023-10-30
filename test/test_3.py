from src.Ejercicio3 import leeCadena, leeLetra, cuenta
import pytest

def test_leecadena(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Hola mundo")
    assert leeCadena() == "Hola mundo"

def test_leeletra(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "o")
    assert leeLetra() == "o"

def test_leeletra_error(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    with pytest.raises(IndexError):
        leeLetra()
def test_cuenta():
    assert cuenta("Hola mundo", "o") == 2