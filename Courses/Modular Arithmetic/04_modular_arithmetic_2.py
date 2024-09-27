def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/modular/ma1/
    According to Fermat's little theorem:
    a⁽ᴾ⁻¹⁾ ≡ 1 mod p <=> a⁽ᴾ⁻¹⁾ % p = 1

    :return: Flag
    """

    a = 273246787654
    p = 65537

    return pow(a, p - 1, p)


if __name__ == '__main__':
    print(get_flag())
