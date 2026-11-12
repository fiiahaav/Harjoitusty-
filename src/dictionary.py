def lue_sanakirja():
    with open ("data/kaikkisanat.txt", "r", encoding="utf-8") as tiedosto:
        sanat = tiedosto.read().splitlines()

    return sanat