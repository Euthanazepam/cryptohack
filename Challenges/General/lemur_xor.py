import numpy as np
from PIL import Image
from os.path import exists
from requests import get

base_url = "https://cryptohack.org"
path = "static/challenges"
filenames = ["lemur_ed66878c338e662d3473f0d98eedbd0d.png", "flag_7ae18c704272532658c10b5faad06d74.png"]


def download_images() -> None:
    """
    Downloads task images.
    """

    for filename in filenames:
        url = f"{base_url}/{path}/{filename}"

        response = get(url=url)

        try:
            with open(f"General/{filename}", "wb") as f:
                f.write(response.content)
        except FileNotFoundError:
            with open(f"{filename}", "wb") as f:
                f.write(response.content)


def xor_images() -> None:
    """
    XOR — https://cryptohack.org/challenges/general/

    Performing a visual XOR between the RGB bytes of the two images.
    """

    if not exists(f"{filenames[0]}") or not exists(f"{filenames[1]}"):
        download_images()

    # Open images.
    img1 = Image.open(filenames[0])
    img2 = Image.open(filenames[1])

    # Make into Numpy arrays.
    img1np = np.array(img1) * 255
    img2np = np.array(img2) * 255

    # XOR with Numpy.
    result = np.bitwise_xor(img1np, img2np).astype(np.uint8)

    # Convert back to PIL image and save.
    Image.fromarray(result).save('result.png')


if __name__ == "__main__":
    xor_images()
