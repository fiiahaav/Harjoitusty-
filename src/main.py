from levenshtein import laske_etaisyys

taulukko = laske_etaisyys("kissa", "kisa")

for rivi in taulukko:
    print(rivi)