from pwn import xor


def get_flag() -> str:
    """
    Returns the challenge flag https://cryptohack.org/courses/intro/xorkey1/
    Two things are known:
        1. Text of message.
        2. The beginning of flag is b"crypto{".
    So, secret_key = message ⊕ b"crypto{".

    :return: Flag
    """

    hex_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

    message = bytes.fromhex(hex_string)

    expected_result = b"crypto{"

    # This fucking piece of shit is needed to remove the '+' symbol from the secret key.
    # Yes, I know. This is a very clumsy method.
    secret_key = xor(message[:9], expected_result).decode("utf-8").replace('+', '').encode()

    flag = xor(message, secret_key).decode("utf-8")

    return flag


if __name__ == "__main__":
    print(get_flag())
