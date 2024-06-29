def get_flag() -> str:
    """
    https://cryptohack.org/courses/intro/enc1/
    """

    ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

    flag = ''.join(chr(o) for o in ords)

    return flag


if __name__ == '__main__':
    print(get_flag())
