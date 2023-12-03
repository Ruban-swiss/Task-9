"""
Method 1:
def fibonacci(count):
    fib_list = [0, 1]

    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, count)))

    return fib_list[:count]


print(fibonacci(11))
"""
##Method 2:


def fibonnaci(n):
    f1 = 0
    f2 = 1

    for i in range(1, n + 1):
        yield f1
        f1, f2 = f2, f1 + f2


for i in fibonnaci(11):
    print(i)
