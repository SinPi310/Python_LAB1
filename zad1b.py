import os

def wypisz_pliki_w_katalogu(sciezka):

    for sciezka_katalogu, podkatalogi, pliki in os.walk(sciezka):
                for plik in pliki:
                    sciezka_pelna = os.path.join(sciezka_katalogu,plik)
                    print(sciezka_pelna)

sciezka = r'C:\student\JS_WH Python\LAB1\LAB1\.idea'
wypisz_pliki_w_katalogu(sciezka)