def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/modular/ma0/
    If a ≡ b mod m, then b = a % m

    :return: Flag
    """

    x = 11 % 6
    y = 8146798528947 % 17

    return min(x, y)


if __name__ == "__main__":
    print(get_flag())
