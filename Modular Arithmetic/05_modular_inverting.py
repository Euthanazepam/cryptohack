def get_flag() -> int:
    """
    https://cryptohack.org/courses/modular/mdiv/
    """

    a = 3
    p = 13

    """
    See https://algorithmica.org/ru/reciprocal.
    If:
        a - integer,
        a^(-1) - inverse of an element a,
        p - prime,
    Then a^(-1) = a^(p - 2) % p
    """

    return (a ** (p - 2)) % p


if __name__ == '__main__':
    print(get_flag())
