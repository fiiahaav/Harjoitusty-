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

    # Täytetään loput taulukosta
    for i in range(1, rivit):
        for j in range(1, sarakkeet):

            if sana1[i-1] == sana2[j-1]:
                kustannus = 0
            else:
                kustannus = 1

            taulukko[i][j] = min(
                taulukko[i - 1][j] + 1,              # poisto
                taulukko[i][j - 1] + 1,              # lisäys
                taulukko[i - 1][j - 1] + kustannus  # korvaus
            )

            if ( 
                i > 1
                and j > 1
                and sana1[i - 1] == sana2[j - 2]
                and sana1[i - 2] == sana2[j - 1]
            ):
                taulukko[i][j] = min(
                    taulukko[i][j],
                    taulukko[i-2][j-2] + 1
                )

    return taulukko[rivit - 1][sarakkeet - 1]