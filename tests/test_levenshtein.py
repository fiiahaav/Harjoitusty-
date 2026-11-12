def test_samat_sanat():
    assert laske_etaisyys("kissa", "kissa") == 0

def test_yksi_poisto():
    assert laske_etaisyys("kissa", "kisa") == 1