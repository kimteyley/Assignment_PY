p = int(input("the amount of money you being with :"))
r = int(input("your annual interest rate % will be? :"))
f = r / 100
t = int(input("how many years will it be? :"))
n = int(input('Annually compound of the interest? :'))
if t < 0:
    print('error')
elif n < 0:
    print('error')
elif p < 0:
    print('error')
elif f < 0:
    print('error')
elif t < 0:
    print('error')
print('the amount of money you will get after', t, 'is', p * ((1 + (f / n)) ** (n * t)))


