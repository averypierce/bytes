import timeit
from typing import Union
from decimal import Decimal


import numpy as np

# performance tests


def count_zeros_after_decimal_numpy(num: Union[int, float]) -> int:
    count = 0
    num = np.array(num)
    while num < 1:
        num *= 10
        if num < 1:
            count += 1
    return count


# Original function
def count_zeros_after_decimal_original(num: Union[int, float]) -> int:
    if num == 0:
        return 0
    count = 0
    while num < 1:
        num *= 10
        if num < 1:
            count += 1
    return count


# Refactored function
def count_zeros_after_decimal_refactored(num: Union[int, float]) -> int:
    str_num = str(num)
    if "." not in str_num:
        return 0
    decimal_part = str_num.split(".")[1]
    return len(decimal_part) - len(decimal_part.lstrip("0"))


# Refactored function
def count_zeros_after_decimal_decimal(num: Union[int, float]) -> int:
    dec = Decimal(str(num))
    return -dec.as_tuple().exponent if dec != 0 else 0


# Test data
test_data = [0.0001, 0.01, 0.1, 0.00000001]

# Number of iterations
iterations = 100000

# Time original function
start_time = timeit.default_timer()
for _ in range(iterations):
    for num in test_data:
        count_zeros_after_decimal_original(num)
end_time = timeit.default_timer()
print(f"Original function took {end_time - start_time} seconds")

# Time refactored function
start_time = timeit.default_timer()
for _ in range(iterations):
    for num in test_data:
        count_zeros_after_decimal_refactored(num)
end_time = timeit.default_timer()
print(f"Refactored function took {end_time - start_time} seconds")

# Time decimal refactored function
start_time = timeit.default_timer()
for _ in range(iterations):
    for num in test_data:
        count_zeros_after_decimal_decimal(num)
end_time = timeit.default_timer()
print(f"Decimal Refactored function took {end_time - start_time} seconds")

# Time numpy function
start_time = timeit.default_timer()
for _ in range(iterations):
    for num in test_data:
        count_zeros_after_decimal_numpy(num)
end_time = timeit.default_timer()
print(f"Numpy function took {end_time - start_time} seconds")


import timeit
from dataclasses import dataclass
from typing import Union


# Original class
class BytesOriginal:
    label = "B"
    pow = 0

    def __init__(self, value: Union[int, float]) -> None:
        self.value = value * 1024**self.pow


# Refactored class
@dataclass
class BytesRefactored:
    value: Union[int, float]
    label: str = "B"
    pow: int = 0

    def __post_init__(self):
        self.value *= 1024**self.pow


# Test data
test_data = [1, 1024, 1048576, 1073741824]

# Time original class
start_time = timeit.default_timer()
for num in test_data:
    BytesOriginal(num)
end_time = timeit.default_timer()
print(f"Original class took {end_time - start_time} seconds")

# Time refactored class
start_time = timeit.default_timer()
for num in test_data:
    BytesRefactored(num)
end_time = timeit.default_timer()
print(f"Refactored class took {end_time - start_time} seconds")
