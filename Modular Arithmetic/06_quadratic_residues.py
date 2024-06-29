def get_flag() -> int:
    """
    https://cryptohack.org/courses/modular/root0/
    """

    p = 29
    ints = [14, 6, 11]
    x = []  # List of square roots

    for a in range(0, p + 1):
        if (a ** 2) % p in ints:
            x.append(a)

    return min(x)


if __name__ == '__main__':
    print(get_flag())
