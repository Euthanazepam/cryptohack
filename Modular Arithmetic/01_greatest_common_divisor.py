def get_flag() -> int:
    """
    https://cryptohack.org/courses/modular/gcd/
    """

    a = 66528
    b = 52920

    while a != b:
        if a > b:
            a -= b  # a = a - b
        else:
            b -= a  # b = b - a

    return a


if __name__ == '__main__':
    print(get_flag())
