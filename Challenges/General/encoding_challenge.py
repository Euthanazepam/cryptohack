import base64
import codecs
import json
import socket

host = "socket.cryptohack.org"
port = 13377


def decode_base64(encoded: str) -> dict:
    """
    Returns json with the decoded message.

    :param encoded: Base64 encoded message received from socket
    :return: json, decoded message
    """

    flag = base64.b64decode(encoded.encode()).decode('utf-8')

    return {"decoded": flag}


def decode_bigint(encoded: str) -> dict:
    """
    Returns json with the decoded message.

    :param encoded: Bigint encoded message received from socket
    :return: json, decoded message
    """

    flag = bytes.fromhex(encoded[2:]).decode('utf-8')

    return {"decoded": flag}


def decode_hex(encoded: str) -> dict:
    """
    Returns json with the decoded message.

    :param encoded: Hex encoded message received from socket
    :return: json, decoded message
    """

    flag = bytes.fromhex(encoded).decode('utf-8')

    return {"decoded": flag}


def decode_rot13(encoded: str) -> dict:
    """
    Returns json with the decoded message.

    :param encoded: ROT13 encoded message received from socket
    :return: json, decoded message
    """

    flag = codecs.encode(encoded, "rot_13")

    return {"decoded": flag}


def decode_utf8(encoded: list) -> dict:
    """
    Returns json with the decoded message.

    :param encoded: UTF-8 encoded message received from socket
    :return: json, decoded message
    """

    flag = ''.join(chr(o) for o in encoded)

    return {"decoded": flag}


def get_flag() -> None:
    """
    Encoding — https://cryptohack.org/challenges/general/
    """

    s = socket.socket()
    s.connect((host, port))

    while True:
        data = s.recv(1024).decode("utf-8")
        parsed_data = json.loads(data)
        try:
            if parsed_data["type"] == "base64":
                decoded = json.dumps(decode_base64(parsed_data["encoded"]))
                print(decoded)
                s.send(decoded.encode())
            elif parsed_data["type"] == "bigint":
                decoded = json.dumps(decode_bigint(parsed_data["encoded"]))
                print(decoded)
                s.send(decoded.encode())
            elif parsed_data["type"] == "hex":
                decoded = json.dumps(decode_hex(parsed_data["encoded"]))
                print(decoded)
                s.send(decoded.encode())
            elif parsed_data["type"] == "rot13":
                decoded = json.dumps(decode_rot13(parsed_data["encoded"]))
                print(decoded)
                s.send(decoded.encode())
            elif parsed_data["type"] == "utf-8":
                decoded = json.dumps(decode_utf8(parsed_data["encoded"]))
                print(decoded)
                s.send(decoded.encode())
            else:
                print(f"{data}")
        except KeyError:
            print(parsed_data)


if __name__ == "__main__":
    get_flag()