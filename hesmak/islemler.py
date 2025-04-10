"""Dört işlemlerin tanımlandığı modül."""


def topla(sayi_1, sayi_2):
    print("Toplama işlemi başarılı bir şekilde yapıldı.")
    return sayi_1 + sayi_2


def cikar(sayi_1, sayi_2):
    print("Çıkarma işlemi başarılı bir şekilde yapıldı.")
    return sayi_1 - sayi_2


def carp(sayi_1, sayi_2):
    print("Çarpma işlemi başarılı bir şekilde yapıldı.")
    return sayi_1 * sayi_2


def bol(sayi_1, sayi_2):
    print("Bölme işlemi başarılı bir şekilde yapıldı.")
    try:
        sonuc = sayi_1 / sayi_2
    except ZeroDivisionError:
        sonuc = f"{sayi_1} 0'a bölünemez!"
    return sonuc
