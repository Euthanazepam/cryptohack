from Crypto.Util.number import long_to_bytes
from requests import get

base_url = "https://cryptohack.org"
path = "static/challenges"
filename = "output_086036e35349a406b94bfac9a7af6cca"
filetype = "txt"


def download_output_txt() -> None:
    """
    Downloads the task file.
    """

    url = f"{base_url}/{path}/{filename}.{filetype}"

    response = get(url=url)

    try:
        with open(f"Public-Key Cryptography/{filename}.{filetype}", "wb") as f:
            f.write(response.content)
    except FileNotFoundError:
        with open(f"{filename}.{filetype}", "wb") as f:
            f.write(response.content)


def get_flag() -> str:
    """
    Returns the challenge flag https://cryptohack.org/courses/public-key/monoprime/

    :return: Flag
    """

    download_output_txt()

    try:
        with open(f"Public-Key Cryptography/{filename}.{filetype}", "r") as f:
            output = f.readlines()
    except FileNotFoundError:
        with open(f"{filename}.{filetype}", "r") as f:
            output = f.readlines()

    N = int(output[0][4:].replace('\n', '').rstrip())
    e = int(output[1][4:].replace('\n', '').rstrip())
    c = int(output[2][5:].replace('\n', '').rstrip())

    # If N is a prime, then φ(N) = N - 1
    phi = N - 1

    d = pow(e, -1, phi)

    m = pow(c, d, N)

    flag = long_to_bytes(m).decode()

    return flag


if __name__ == "__main__":
    print(get_flag())
