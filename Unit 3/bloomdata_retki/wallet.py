from typing_extensions import runtime


class Wallet:
    def __init__(self, init_balance) -> None:
        self.balance = init_balance
        self.color = 'black'

    def add(self,amount):
        self.balance += amount

    def spend(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError("Insufficient Funds")


class SmallWallet(Wallet):
    cap = 100

    def __init__(self, init_balance) -> None:
        self.balance = init_balance
        self.color = 'black'
        super().__init__
    def add(self,amount):
        if (self.balance + amount) > self.cap:
            raise RuntimeError("Wallet is full")
        else:
            self.balance += amount