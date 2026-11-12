def laske_etaisyys(sana1, sana2):
    rivit = len(sana1) + 1
    sarakkeet = len(sana2) + 1

    taulukko = []

    for i in range(rivit):
        rivi = [0] * sarakkeet
        taulukko.append(rivi)

    return taulukko