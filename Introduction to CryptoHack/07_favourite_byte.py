from pwn import xor


def get_flag() -> str:
    """
    https://cryptohack.org/courses/intro/xorkey0/
    """

    hex_string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

    message = bytes.fromhex(hex_string)

    for k in range(256):
        secret_byte = k.to_bytes()
        flag = xor(message, secret_byte).decode('utf-8')
        if 'crypto' in flag:
            print(f'Secret byte: {secret_byte}')

            return flag


if __name__ == '__main__':
    print(get_flag())
