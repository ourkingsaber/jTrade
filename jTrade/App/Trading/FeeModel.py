
from abc import ABCMeta, abstractmethod


class FeeModel(metaclass=ABCMeta):
    """Fee Model calculator."""

    @abstractmethod
    def calculate(self, share, price):
        """Calculates fee"""
        return


class FixedFlat(FeeModel):
    """Charges a flat rate for each order"""

    def __init__(self, flat_rate=0):
        self.flat_rate = flat_rate

    def calculate(self, share, price):
        return self.flat_rate


class FixedRatio(FeeModel):
    """Charges a fixed ratio for each order"""

    def __init__(self, flat_rate, cap=None, floor=None):
        self.flat_rate = flat_rate
        self.cap = cap
        self.floor = floor

    def calculate(self, share, price):
        fee = share * price * self.flat_rate
        if self.cap is not None:
            fee = min(fee, self.cap)
        if self.floor is not None:
            fee = max(fee, self.floor)
        return fee
