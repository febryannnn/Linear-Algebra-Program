import numpy as np
from decimal import Decimal, ROUND_HALF_UP

def round(n, decimals=0):
    d = Decimal(str(n))
    return float(d.quantize(Decimal('1.' + '0' * decimals), rounding=ROUND_HALF_UP))

print(round_up(1.425, 2))

# print(np.round_up(1.435, 2))