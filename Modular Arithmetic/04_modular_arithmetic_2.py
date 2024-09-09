def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/modular/ma1/

    :return: Flag
    """

    a = 273246787654
    p = 65537

    """
    According to Fermat's little theorem:
    a^(p-1) ≡ 1 mod p <=> a^(p-1) % p = 1
    """

    return pow(a, p - 1, p)


if __name__ == '__main__':
    print(get_flag())
