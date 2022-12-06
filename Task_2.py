import sympy

with open('file.txt', 'r') as data:
    poly_1 = data.read()
print(poly_1)

with open('file_2.txt', 'r') as data:
    poly_2 = data.read()
print(poly_2)

a = poly_1[:-3]
b = poly_2[:-3]
add = "+"
a += add

x = sympy.Symbol('x')
result = sympy.sympify(a + b)
print(f'{result} = 0')
with open('file_res.txt', 'w') as res:
    res.write(f'{result} = 0')
