def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/public-key/rsa_starter_1/

    :return: Flag
    """

    return pow(101, 17, 22663)


if __name__ == "__main__":
    print(get_flag())
