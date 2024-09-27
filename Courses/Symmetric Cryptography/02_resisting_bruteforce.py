def get_flag() -> str:
    """
    Returns the challenge flag https://cryptohack.org/courses/symmetric/aes1/

    References:
        1. https://en.wikipedia.org/wiki/Biclique_attack

    :return: Flag
    """

    return "crypto{biclique}"


if __name__ == "__main__":
    print(get_flag())
