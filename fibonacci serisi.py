print(""""
*****
Fibonacci Serisi Bulma Programina Hosgeldiniz
*****
""")

a=1
b=1
fibonacci = [a,b]
x = int(input("Kac elemanli bir fibonacci seri olusturmak istersiniz?:"))

for i in range(x-2):
    a,b=b,a+b

    fibonacci.append(b)

print(fibonacci)
