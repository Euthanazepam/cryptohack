from factordb.factordb import FactorDB
from os.path import exists
from requests import get

base_url = "https://cryptohack.org"
path = "static/challenges"
filename = "output_cf39018a5db981bd454ddcdcf6595167"
filetype = "txt"


def download_output_txt() -> None:
    """
    Downloads the task file.
    """

    url = f"{base_url}/{path}/{filename}.{filetype}"

    response = get(url=url)

    try:
        with open(f"RSA/{filename}.{filetype}", "wb") as f:
            f.write(response.content)
    except FileNotFoundError:
        with open(f"{filename}.{filetype}", "wb") as f:
            f.write(response.content)


def get_flag() -> str:
    """
    Primes part 1 — https://cryptohack.org/challenges/rsa/

    :return: Flag
    """

    if not exists(f"{filename}.{filetype}"):
        download_output_txt()

    with open(f"{filename}.{filetype}", "r") as f:
            output = f.readlines()

    n = int(output[0][4:].replace('\n', '').rstrip())
    e = int(output[1][4:].replace('\n', '').rstrip())
    c = int(output[2][5:].replace('\n', '').rstrip())

    # Use http://factordb.com to factorize n
    f = FactorDB(n)
    f.connect()
    p, q = f.get_factor_list()

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    m = pow(c, d, n)

    flag = m.to_bytes(c.bit_length() // 8, 'big')[2:].decode()

    return flag


if __name__ == "__main__":
    print(get_flag())
