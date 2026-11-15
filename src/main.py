from dictionary import lue_sanakirja, etsi_parhaat_ehdotukset


def main():
    sanat = lue_sanakirja()

    syote = input("Anna sana: ")

    ehdotukset = etsi_parhaat_ehdotukset(syote, sanat)

    print("\nTarkoititko:")

    for i, (_, sana) in enumerate(ehdotukset, start=1):
        print(f"{i}. {sana}")


if __name__ == "__main__":
    main()