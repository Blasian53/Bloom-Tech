from bloomdata_retki.wallet import Wallet
import pytest


@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixure
def wallet_100():
    return Wallet(100)

def test_init_empty_wallet(empty_wallet):
    assert empty_wallet.balance == 0

def test_init_add(empty_wallet):
    empty_wallet.add(25)
    assert empty_wallet.balance == 25

def test_init_spend(wallet_100):
    wallet_100.spend(25)
    assert wallet_100.balance == 75

def test_init_color(empty_wallet):
    assert empty_wallet.color == 'black'