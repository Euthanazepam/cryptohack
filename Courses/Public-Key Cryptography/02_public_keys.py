def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/public-key/rsa_starter_2/

    :return: Flag
    """

    m = 12

    p = 17
    q = 23

    e = 65537

    n = p * q

    return pow(m, e, n)


if __name__ == "__main__":
    print(get_flag())
