from typing import Union

def count_zeros_after_decimal(num: Union[int, float]) -> int:
    if num == 0:
        return 0
    count = 0
    while num < 1:
        num *= 10
        if num < 1:
            count += 1
    return count

def rounder(val: float, decimal_places: int = 3) -> float:
    if val > 1:
        return round(val)
    zero_count = count_zeros_after_decimal(val)
    return round(val, max(decimal_places, zero_count))

class Bytes:
    label = 'B'
    pow = 0

    def __init__(self, value: Union[int, float]) -> None:
        self.value = value * 1024 ** self.pow

    def __str__(self) -> str:
        u_value = self.value / 1024 ** self.pow
        zeros = count_zeros_after_decimal(u_value)
        return f'{rounder(u_value):.{zeros}f} {self.label}'

    @classmethod
    def from_bytes(cls, value: Union[int, float]) -> 'Bytes':
        instance = cls.__new__(cls)
        instance.value = value
        return instance

    @property
    def b(self):
        return Bytes.from_bytes(self.value)

    @property
    def kb(self):
        return Kilobytes.from_bytes(self.value)

    @property
    def mb(self):
        return Megabytes.from_bytes(self.value)

    @property
    def gb(self):
        return Gigabytes.from_bytes(self.value)

    @property
    def tb(self):
        return Terabytes.from_bytes(self.value)


class Kilobytes(Bytes):
    label = 'KB'
    pow = 1

class Megabytes(Bytes):
    label = 'MB'
    pow = 2

class Gigabytes(Bytes):
    label = 'GB'
    pow = 3

class Terabytes(Bytes):
    label = 'TB'
    pow = 4
