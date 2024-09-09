from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long
from requests import get

base_url = "https://cryptohack.org"
path = "static/challenges"
filename = "private_0a1880d1fffce9403686130a1f932b10"
filetype = "key"


def download_private_key() -> None:
    """
    Downloads a file with a private key.
    """

    url = f"{base_url}/{path}/{filename}.{filetype}"

    response = get(url=url)

    try:
        with open(f"Public-Key Cryptography/{filename}.{filetype}", "wb") as f:
            f.write(response.content)
    except FileNotFoundError:
        with open(f"{filename}.{filetype}", "wb") as f:
            f.write(response.content)


def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/public-key/rsa_starter_6/

    :return: Flag
    """

    download_private_key()

    try:
        with open(f"Public-Key Cryptography/{filename}.{filetype}", "r") as f:
            key = f.readlines()
    except FileNotFoundError:
        with open(f"{filename}.{filetype}", "r") as f:
            key = f.readlines()

    N = int(key[0][4:].replace('\n', ''))
    d = int(key[1][4:].replace('\n', ''))

    m = "crypto{Immut4ble_m3ssag1ng}"

    # Calculate the SHA256 hash of the message
    H = SHA256.new(m.encode()).digest()

    s = pow(bytes_to_long(H), d, N)

    return s


if __name__ == "__main__":
    print(get_flag())
