# Вычислить число Pi c заданной точностью d, не используя ф. round()
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from decimal import Decimal


d = 0.001
num = Decimal(math.pi)
# print(num)
# p1 = str(d).split(".")[1]
# print(p1)
# p2 = len(p1)
# print(p2)
# p3 = "0" * p2
# print(p3)
num = num.quantize(Decimal("1."+"0"* len(str(d).split(".")[1])))
print(num)
