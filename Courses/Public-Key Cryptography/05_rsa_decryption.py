def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/public-key/rsa_starter_5/

    :return: Flag
    """

    # The task uses a private key from https://cryptohack.org/courses/public-key/rsa_starter_4/
    N = 882564595536224140639625987659416029426239230804614613279163
    e = 65537

    p = 857504083339712752489993810777
    q = 1029224947942998075080348647219
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    c = 77578995801157823671636298847186723593814843845525223303932

    return pow(c, d, N)


if __name__ == "__main__":
    print(get_flag())
