import math
from math import log2
from typing import List


def entropy(class_probabilities: List[float]) -> float:
    """
    Вычислите энтропию как сумму следующих величин: -p_i*log2(p_i)

    Договоримся, что, если p_i == 0, то -p_i*log2(p_i) = 0

    Длина списка: len(class_probabilities)
    """