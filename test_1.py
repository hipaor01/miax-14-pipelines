import mimodulo


def test_example():
    valor = mimodulo.sumar(2, 3)
    print(f"Resultado de la suma: {valor}")
    assert valor == 4
