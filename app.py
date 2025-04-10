from hesmak import hesap_makinesi

cikis_yapildi_mi = False
while not cikis_yapildi_mi:
    print('[1]: Toplama', '[2]: Çıkarma', '[3]: Çarpma', '[4]: Bölme', sep='\n')
    secenek = input("Bir seçenek giriniz (Çıkış için 0'a basınız): ")
    if secenek == '0':
        print('Program başarılı bir şekilde sonlandırılmıştır.')
        cikis_yapildi_mi = True
    elif secenek == '1' or secenek == '2' or secenek == '3' or secenek == '4':
        birinci_sayi = float(input('Birinci sayıyı giriniz: '))
        ikinci_sayi = float(input('İkinci sayıyı giriniz: '))
        if ikinci_sayi == 0.0 and secenek == '4':
            print("Hatalı bölme işlemi. Baştan başlıyor...")
            continue
        print(f"Sonuç: {hesap_makinesi(birinci_sayi, ikinci_sayi, int(secenek))}")
        print("Hesaplama başarılı. Yeniden başlatılıyor.")
    else:
        print('Hatalı seçenek girdiniz!')
