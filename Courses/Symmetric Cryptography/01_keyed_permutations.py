def get_flag() -> str:
    """
    Returns the challenge flag https://cryptohack.org/courses/symmetric/aes0/

    References:
        1. https://en.wikipedia.org/wiki/Bijection

    :return: Flag
    """

    return "crypto{bijection}"


if __name__ == "__main__":
    print(get_flag())
