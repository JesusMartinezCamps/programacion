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

def test_Yatzy():
    resultado = 50
    assert resultado == Yatzy.yatzy(1, 1, 1, 1, 1)

def test_ones():
    assert 3 == Yatzy.ones(1, 1, 2, 1, 6)
    assert 0 == Yatzy.ones(3, 2, 2, 5, 5)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)

def test_twos():
    assert 2 == Yatzy.twos(2, 1, 1, 1, 1)
    assert 4 == Yatzy.twos(2, 2, 1, 1, 1)
    assert 6 == Yatzy.twos(2, 2, 2, 1, 1)

def test_threes():
    assert 3 == Yatzy.threes(3, 1, 1, 2, 5)
    assert 0 == Yatzy.threes(6, 1, 4, 2, 5)
    assert 9 == Yatzy.threes(3, 3, 3, 2, 5)


@pytest.fixture

def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 6, 4, 5)
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

def test_pair():
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.pair(1, 2, 3, 4, 5)

def test_two_pair():
    assert 8 == Yatzy.two_pair(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pair(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pair(1, 1, 2, 2, 2)
    assert 12 == Yatzy.two_pair(1, 3, 3, 3, 3)
    assert 12 == Yatzy.two_pair(3, 3, 3, 3, 3)

def test_three_of_a_kind():
    assert 3 == Yatzy.three_of_a_kind(1, 1, 1, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 12 == Yatzy.three_of_a_kind(4, 4, 4, 4, 1)
    assert 18 == Yatzy.three_of_a_kind(6, 6, 6, 6, 6)

def test_four_of_a_kind():
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)

def test_small_straight():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.small_straight(3, 2, 1, 5, 4)
    assert 0 == Yatzy.small_straight(3, 2, 1, 5, 5)

def test_large_straight():
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 20 == Yatzy.large_straight(3, 2, 6, 5, 4)
    assert 0 == Yatzy.large_straight(3, 2, 6, 6, 5)
