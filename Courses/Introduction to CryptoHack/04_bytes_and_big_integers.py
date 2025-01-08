from Crypto.Util.number import long_to_bytes


def get_flag() -> str:
    """
    Returns the challenge flag https://cryptohack.org/courses/intro/enc4/

    :return: Flag
    """

    integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

    flag = long_to_bytes(integer).decode("utf-8")

    return flag


if __name__ == "__main__":
    print(get_flag())
