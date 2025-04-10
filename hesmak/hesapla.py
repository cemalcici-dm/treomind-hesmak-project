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
