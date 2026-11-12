from dictionary import lue_sanakirja
from levenshtein import laske_etaisyys

sanat = lue_sanakirja()

print(f"Sanoja löytyi: {len(sanat)}")
# print(sanat[:10])

taulukko = laske_etaisyys("kissa", "kisa")

for rivi in taulukko:
    print(rivi)