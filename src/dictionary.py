from levenshtein import laske_etaisyys

def lue_sanakirja():
    # Lukee sanat tiedostosta ja palauttaa ne listana
    with open ("data/allwords.txt", "r", encoding="utf-8") as tiedosto:
        return tiedosto.read().splitlines()

def etsi_parhaat_ehdotukset(syote, sanat, maara=5):
    ehdotukset = []

    for sana in sanat:
        etaisyys = laske_etaisyys(syote, sana)
        ehdotukset.append((etaisyys, sana))

    ehdotukset.sort()

    return ehdotukset[:maara]