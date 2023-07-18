from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar.deposit(2)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(2)
    assert jar.size == 4
    jar.withdraw(2)
    assert jar.size == 2

def test_Val_Er():
    jar = Jar()
    jar.n = 15
    jar.size == "Exceed Capacity"
