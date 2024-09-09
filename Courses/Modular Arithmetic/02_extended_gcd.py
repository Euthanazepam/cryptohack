def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/modular/egcd/

    :return: Flag
    """

    a = 26513
    b = 32321

    # Snatch from https://brilliant.org/wiki/extended-euclidean-algorithm.
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b

    # return gcd, x, y
    return min(x, y)


if __name__ == '__main__':
    print(get_flag())
