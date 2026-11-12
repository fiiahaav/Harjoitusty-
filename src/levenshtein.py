def laske_etaisyys(sana1, sana2):
    rivit = len(sana1) + 1
    sarakkeet = len(sana2) + 1

    taulukko = []

    for i in range(rivit):
        taulukko.append([0] * sarakkeet)

    # Ensimmäinen sarake
    for i in range(rivit):
        taulukko[i][0] = i

    # Ensimmäinen rivi
    for j in range(sarakkeet):
        taulukko[0][j] = j

    return taulukko