from decimal import *
getcontext().prec = 101
def calc (prec = 80):
    pi = Decimal(0)
    for k in range (prec):
        pi = pi + Decimal( (Decimal(1)/Decimal(16**k))*( (Decimal(4)/Decimal(8*k+1))-(Decimal(2)/Decimal(8*k+4))-(Decimal(1)/Decimal(8*k+5))-(Decimal(1)/Decimal(8*k+6)) ) )
    print (pi)
calc()

