from src.Ejercicio1 import leeCadena, invierteCadena, generaMensaje
import pytest

def test_leeCadena(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Hola mundo")
    assert leeCadena() == "Hola mundo"

def test_invierteCadena():
    assert invierteCadena("Hola mundo") == "odnum aloH"
    
def test_generaMensaje():
    assert generaMensaje("odnum aloH") == "La palabra invertida es: odnum aloH"