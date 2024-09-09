def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/public-key/rsa_starter_3/

    :return: Flag
    """

    p = 857504083339712752489993810777
    q = 1029224947942998075080348647219

    phi = (p - 1) * (q - 1)

    return phi


if __name__ == "__main__":
    print(get_flag())
