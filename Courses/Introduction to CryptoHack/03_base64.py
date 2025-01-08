import base64


def get_flag() -> str:
    """
    Returns the challenge flag https://cryptohack.org/courses/intro/enc3/

    :return: Flag
    """

    hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

    flag = base64.b64encode(bytes.fromhex(hex_string)).decode("utf-8")

    return flag


if __name__ == "__main__":
    print(get_flag())
