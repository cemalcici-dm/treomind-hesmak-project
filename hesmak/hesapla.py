"""Dört işlem yapan hesap makinesi modülü"""

from .islemler import (
    topla,
    cikar,
    carp,
    bol
)


def hesap_makinesi(sayi_1, sayi_2, secenek):
    islem = {
        1: topla,
        2: cikar,
        3: carp,
        4: bol
    }.get(secenek)
    
    return islem(sayi_1, sayi_2)


if __name__ == '__main__':
    print(hesap_makinesi(5, 3, 1))
    print(hesap_makinesi(5, 3, 2))
    print(hesap_makinesi(5, 3, 3))
    print(hesap_makinesi(5, 3, 4))
