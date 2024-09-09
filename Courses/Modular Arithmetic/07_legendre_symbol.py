from requests import get

base_url = "https://cryptohack.org"
path = "static/challenges"
filename = "output_479698cde19aaa05d9e9dfca460f5443"
filetype = "txt"


def download_output_txt() -> None:
    """
    Downloads the task file.
    """

    url = f"{base_url}/{path}/{filename}.{filetype}"

    response = get(url=url)

    try:
        with open(f"Modular Arithmetic/{filename}.{filetype}", "wb") as f:
            f.write(response.content)
    except FileNotFoundError:
        with open(f"{filename}.{filetype}", "wb") as f:
            f.write(response.content)


def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/modular/root1/

    :return: Flag
    """

    download_output_txt()

    try:
        with open(f"Modular Arithmetic/{filename}.{filetype}", "r") as f:
            output = f.readlines()
    except FileNotFoundError:
        with open(f"{filename}.{filetype}", "r") as f:
            output = f.readlines()

    p = int(output[0][4:].replace('\n', '').rstrip())

    # Convert all strings in a list to int
    ints = list(map(int, output[2][8:-2].replace('\n', '').rstrip().split(', ')))

    for a in ints:
        if pow(a, (p - 1) // 2, p) == 1:    # It's a quadratic residue
            return pow(a, (p + 1) // 4, p)  # It's the square root of a quadratic residue


if __name__ == "__main__":
    print(get_flag())
