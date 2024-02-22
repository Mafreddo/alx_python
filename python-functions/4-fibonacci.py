def fibonacci_sequence(n):
    fibonacci_list = []
    if n > 0 and isinstance(n, int):
        a = 0
        b = 1
        for i in range(n):
            fibonacci_list.append(a)
            c = a + b
            a = b
            b = c
    return fibonacci_list