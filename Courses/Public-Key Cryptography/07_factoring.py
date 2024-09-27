from factordb.factordb import FactorDB


def get_flag() -> int:
    """
    Returns the challenge flag https://cryptohack.org/courses/public-key/rsa_factoring/

    :return: Flag
    """

    n = 510143758735509025530880200653196460532653147

    # Use http://factordb.com to factorize n
    f = FactorDB(n)
    f.connect()
    p, q = f.get_factor_list()

    return min(p, q)


if __name__ == "__main__":
    print(get_flag())
