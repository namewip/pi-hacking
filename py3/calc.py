import decimal
import math

prec = 7
decimal.getcontext().prec = 2500 * prec


def calcit(maxiter):
    s = decimal.Decimal(0)

    for n in range(maxiter):
        s += (-1) ** n * math.factorial(6 * n) * (13591409 + n * decimal.Decimal(545140134)) / \
            (math.factorial(n) ** 3) / math.factorial(3 * n) / (100100025 * 8 * decimal.Decimal(327843840)) ** n

    return 53360 * decimal.Decimal(640320).sqrt() / s

print(calcit(50 * prec))
