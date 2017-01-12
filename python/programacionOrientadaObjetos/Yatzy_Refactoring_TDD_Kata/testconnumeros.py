def test_fours(inyector):
    # Es necesario un objeto ya creado
    valorEsperado4 = 4
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado4 == inyector.fours()

def test_fives(inyector):
    
    valorEsperado5 = 5

    assert valorEsperado5 == inyector.fives()


def test_sixes(inyector):
    
    valorEsperado6 = 6

    assert valorEsperado6 == inyector.sixes()