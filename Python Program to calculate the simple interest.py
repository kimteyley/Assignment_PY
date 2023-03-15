p = float(input("the amount of money you being with :"))
r = float(input("your annual interest rate %? :"))
f = r/100
t = int(input("how many years will it be? :"))
print('Here is the amount the money you will have after interest:', p * (1 + f*t))