def fibonacci(posicao):
    if posicao == 0:
        return 0

    if posicao == 1:
        return 1

    return fibonacci(posicao - 1) + fibonacci(posicao - 2)


def fibonacci_print(n):
    num_fibonacci = []
    for i in range(n):
        num_fibonacci.append(fibonacci(i))
    print(num_fibonacci)


if __name__ == "__main__":
    fibonacci_print(30)
