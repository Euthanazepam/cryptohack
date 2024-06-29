from pwn import xor


def get_flag() -> str:
    """
    https://cryptohack.org/courses/intro/xor0/
    """

    message = 'label'
    integer = 13

    message = message.encode()
    integer = integer.to_bytes()

    flag = xor(message, integer).decode('utf-8')

    return flag


def get_flag_own_solution() -> str:
    message = 'label'
    integer = 13

    flag = ''

    for char in message:
        flag += chr(ord(char) ^ integer)

    return flag


if __name__ == '__main__':
    print(get_flag())
    # print(get_flag_own_solution())
