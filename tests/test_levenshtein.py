import sys
import os
sys.path.append(os.path.abspath("src"))

from levenshtein import laske_etaisyys


def test_samat_sanat():
    assert laske_etaisyys("kissa", "kissa") == 0


def test_poisto():
    assert laske_etaisyys("kissa", "kisa") == 1


def test_lisays():
    assert laske_etaisyys("kisa", "kissa") == 1


def test_korvaus():
    assert laske_etaisyys("kissa", "kossi") == 1