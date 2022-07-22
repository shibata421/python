#!/usr/bin/python3
def sequence():
    i = 0
    while True:
        i += 1
        yield i


if __name__ == "__main__":
    seq = sequence()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
