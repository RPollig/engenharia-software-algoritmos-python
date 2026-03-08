# 15. Gere os 10 primeiros números da sequência de Fibonacci. Obs.: Não entendi!
# 15. Gere os 10 primeiros números da sequência de Fibonacci.

a = 0
b = 1

for i in range(10):
    print(a)

    proximo = a + b
    a = b
    b = proximo 