import pytest
from yatzy import Yatzy


# Chance
# The player scores the sum of all dice, no matter what they read.

#test porque es un caso test
#chance porque es el nombre de lo que se esta testeando
def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)


@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada


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
