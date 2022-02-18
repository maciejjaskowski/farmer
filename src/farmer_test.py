from farmer import symulacja, wKrolikach, rozmnoz_jeden, rozmnazanie, opcje, wszystkie_zwierzeta, zlicz


def test_symulacja():

    zwierzeta = {
        'maly_pies': 0,
        'duzy_pies': 0,
        'kon': 0,
        'krowa': 2,
        'swinka': 6,
        'owca': 6,
        'krolik': 12
    }
    wyniki = symulacja(zwierzeta=zwierzeta)

    print("Wyniki przed symulacji: ", wKrolikach(zwierzeta))
    print("Wyniki po symulacji: ", wyniki)

def test_rozmnazanie_jeden():
    assert rozmnoz_jeden(zwierzeta=2, zwierzeta_na_kostkach=2) == 4
    assert rozmnoz_jeden(zwierzeta=2, zwierzeta_na_kostkach=1) == 3
    assert rozmnoz_jeden(zwierzeta=2, zwierzeta_na_kostkach=0) == 2
    assert rozmnoz_jeden(zwierzeta=3, zwierzeta_na_kostkach=2) == 5
    assert rozmnoz_jeden(zwierzeta=3, zwierzeta_na_kostkach=1) == 5

def test_rozmnazanie():
    assert rozmnazanie({
        'maly_pies': 0,
        'duzy_pies': 0,
        'kon': 0,
        'krowa': 0,
        'swinka': 0,
        'owca': 0,
        'krolik': 1
    }, wylosowana_kostka1='krolik', wylosowana_kostka2='krolik') == {
        'maly_pies': 0,
        'duzy_pies': 0,
        'kon': 0,
        'krowa': 0,
        'swinka': 0,
        'owca': 0,
        'krolik': 2
    }

    assert rozmnazanie({
        'maly_pies': 0,
        'duzy_pies': 0,
        'kon': 0,
        'krowa': 0,
        'swinka': 1,
        'owca': 2,
        'krolik': 1
    }, wylosowana_kostka1='swinka', wylosowana_kostka2='krolik') == {
        'maly_pies': 0,
        'duzy_pies': 0,
        'kon': 0,
        'krowa': 0,
        'swinka': 2,
        'owca': 2,
        'krolik': 2
    }

def u(z):
    s = {
        'maly_pies': 0,
        'duzy_pies': 0,
        'kon': 0,
        'krowa': 0,
        'swinka': 0,
        'owca': 0,
        'krolik': 0
    }
    for k, v in z.items():
        s[k] = z[k]
    return s

def test_opcje():
    wynik = opcje(6, a=[], d=wszystkie_zwierzeta)
    print(wynik)
    assert wynik == [
        ['owca'],
        ['krolik'] * 6,
    ]

def test_opcje2():
    wynik = opcje(7, a=[], d=wszystkie_zwierzeta)
    print(wynik)
    assert wynik == [
        ['owca', 'krolik'],
        ['krolik'] * 7,
    ]


def test_zliczanie():
    zlicz(['owca', 'owca', 'krolik', 'krolik', 'krolik']) == {
        'owca': 2,
        'krolik': 3,
    }