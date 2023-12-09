def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Change this value to generate a longer or shorter sequence
fibonacci(100000)