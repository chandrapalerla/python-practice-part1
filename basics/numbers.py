from fractions import Fraction

a = int(123.23)
print(a)
b = int('123')
print(b)
c = int('   -12_345\n')
print(c)
d = int('FACE', 16)
print(d)
e = int('0xface', 0)
print(e)
f = int('01110011', base=2)
print(f)

print(f"floting point started::::::")
tax = 12.5 / 100
price = 100.50
var = round(price * tax, 3)
print(f"var = {var}")

print(Fraction(16, -10))

