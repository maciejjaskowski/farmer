import copy
import random
from math import floor


def rozmnazanie(z,
                wylosowana_kostka1,
                wylosowana_kostka2,):
    z = copy.copy(z)
    if (wylosowana_kostka1 == 'wilk'):

        if (z['duzy_pies'] > 0):
            z['duzy_pies'] = z['duzy_pies'] - 1
        else:
            return {
                'maly_pies': z['maly_pies'],
                'duzy_pies': 0,
                'kon': z['kon'],
                'krowa': 0,
                'swinka': 0,
                'owca': 0,
                'krolik': 0
            }

    if (wylosowana_kostka2 == 'lis'):

        if (z['maly_pies'] > 0):
            z['maly_pies'] = z['maly_pies'] - 1
        else:
            z['krolik'] = 0
            return z

    kroliki_na_kostkach = toInt(wylosowana_kostka1 == 'krolik') + toInt(wylosowana_kostka2 == 'krolik')
    owce_na_kostkach = toInt(wylosowana_kostka1 == 'owca') + toInt(wylosowana_kostka2 == 'owca')
    swinki_na_kostkach = toInt(wylosowana_kostka1 == 'swinka') + toInt(wylosowana_kostka2 == 'swinka')

    krowy_na_kostkach = toInt(wylosowana_kostka1 == 'krowa') + toInt(wylosowana_kostka2 == 'krowa')
    konie_na_kostkach = toInt(wylosowana_kostka1 == 'kon') + toInt(wylosowana_kostka2 == 'kon')

    return {
        'maly_pies': z['maly_pies'],
        'duzy_pies': z['duzy_pies'],
        'kon': rozmnoz_jeden(z['kon'], konie_na_kostkach),
        'krowa': rozmnoz_jeden(z['krowa'], krowy_na_kostkach),
        'swinka': rozmnoz_jeden(z['swinka'], swinki_na_kostkach),
        'owca': rozmnoz_jeden(z['owca'], owce_na_kostkach),
        'krolik': rozmnoz_jeden(z['krolik'], kroliki_na_kostkach)
    }


def wKrolikach(z):
    wynik = (z['krolik'] + (((z['kon'] * 2 + (z['krowa'] + z['duzy_pies'] )) * 3 + z['swinka']) * 2 + (z['owca'] + z['maly_pies'])) * 6)
    return wynik


def rozmnoz_jeden(zwierzeta, zwierzeta_na_kostkach):
    if (zwierzeta_na_kostkach > 0):
        return zwierzeta + floor((zwierzeta + zwierzeta_na_kostkach) / 2)
    else:
        return zwierzeta


kostka1 = ["krolik", "krolik", "krolik", "krolik", "wilk", "owca", "owca", "owca", "swinka", "krowa", "krolik",
           "krolik"]
kostka2 = ["krolik", "krolik", "krolik", "krolik", "lis", "owca", "owca", "owca", "swinka", "kon", "krolik", "krolik"]

wszystkie_zwierzeta = [
    {'nazwa': 'owca',
     'wartosc': 6},
    {'nazwa': 'krolik',
     'wartosc': 1},
]

def toInt(b):
    if (b):
        return 1
    else:
        return 0


def opcje(k, a, d):
    if k > 0:
        nowa_lista = []
        for i, z in enumerate(d):
             if k >= z['wartosc']:
                nowa_lista.extend(opcje(k-z['wartosc'], a + [z['nazwa']], d[i:]))
        return nowa_lista
    else:
        return [a]


def symulacja(zwierzeta, N=100000):
    wyniki = 0.
    for j in range(N):
        zwierzeta_rozmnozone = rozmnazanie(
            copy.copy(zwierzeta),
            wylosowana_kostka1=kostka1[random.randint(0, 11)],
            wylosowana_kostka2=kostka2[random.randint(0, 11)],
        )

        wyniki = wyniki + wKrolikach(zwierzeta_rozmnozone)

    return wyniki / N

def zlicz(lista):
    b = 0
    for i in lista:
        if i == 'owca':
            b = b + 1
    a = 0
    for i in lista:
        if i == 'krolik':
            a = a + 1

    return {
        'maly_pies': 0,
        'duzy_pies': 0,
        'kon': 0,
        'krowa': 0,
        'swinka': 0,
        'owca': b,
        'krolik': a
    }


for o in opcje(17, a=[], d=wszystkie_zwierzeta):
    zliczone = zlicz(o)
    print(f"opcja {zliczone}")
    wynik = symulacja(zwierzeta=zliczone)
    print(f"opcja {zliczone}, wynik {wynik}")