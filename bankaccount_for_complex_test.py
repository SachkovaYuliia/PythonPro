class BankAccount:
    
    def __init__(self, initial_balance: float = 0.0):

        """
        Ініціалізує рахунок з початковим балансом.
        """

        self.balance = initial_balance

    def deposit(self, amount: float):

        """
        Поповнює рахунок на вказану суму.
        """

        if amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за 0.")
        self.balance += amount

    def withdraw(self, amount: float):

        """
        Знімає кошти з рахунку, якщо достатньо коштів.
        """

        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за 0.")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.balance -= amount

    def get_balance(self) -> float:

        """
        Повертає поточний баланс рахунку.
        """

        return self.balance
