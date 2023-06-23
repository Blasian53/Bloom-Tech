import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


@pytest.fixture
def product_ex():
    return Product("Test Product")


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_stealability(product_ex):
    assert product_ex.stealability() == "Kinda stealable."


def test_explode(product_ex):
    assert product_ex.explode() == "...boom!"


def test_generator(product_ex):
    assert len(generate_products()) == 30


def test_adjectives(product_ex):
    assert len(ADJECTIVES) == 5


def test_nouns(product_ex):
    assert len(NOUNS) == 5
