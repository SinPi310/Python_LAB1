import os

def zlicz_ilosc_plikow(sciezka_do_katalogu):

    lp = 0
    print (os.listdir(sciezka_do_katalogu))
    for element in os.listdir(sciezka_do_katalogu):
        sciezka_elementu = os.path.join(sciezka_do_katalogu, element)
        if os.path.isfile(sciezka_elementu):
            lp += 1
    return lp

sciezka = r'C:\student\JS_WH Python\LAB1\LAB1\.idea'

lp = zlicz_ilosc_plikow(sciezka)

print(f'Ilosc plikow w katalogu  {sciezka}: {lp}')
