#!/usr/bin/python3
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    print(f'1! = {fatorial(1)}')
    print(f'2! = {fatorial(2)}')
    print(f'3! = {fatorial(3)}')
    print(f'4! = {fatorial(4)}')
    print(f'10! = {fatorial(10)}')
