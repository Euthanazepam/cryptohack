def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/modular/mdiv/
    See https://algorithmica.org/ru/reciprocal.
    If:
        a — integer,
        a⁻¹ — inverse of an element a,
        p — prime,
    Then a⁻¹ = a⁽ᴾ⁻²⁾ % p

    :return: Flag
    """

    a = 3
    p = 13

    return pow(a, p - 2, p)


if __name__ == "__main__":
    print(get_flag())
