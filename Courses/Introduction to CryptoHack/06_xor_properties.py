from pwn import xor # pip install pwntools


def get_flag() -> str:
    """
    Returns the challenge flag https://cryptohack.org/courses/intro/xor1/

    :return: Flag
    """

    key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
    key2 = xor(key1, bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"))
    key3 = xor(key2, bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"))

    flag = xor(xor(xor(key1, key3), key2),
               bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")).decode("utf-8")

    return flag


if __name__ == "__main__":
    print(get_flag())
