import re

def usun_slowa(tekst, slowa_do_usuniecia):

    for slowo in slowa_do_usuniecia:
        tekst = re.sub(rf'\b{re.escape(slowo)}\b', '', tekst, flags=re.IGNORECASE)
    return tekst

def zamien_slowa(tekst, zamiana):

    for slowo, zastepcze_slowo in zamiana.items():
        tekst = re.sub(rf'\b{re.escape(slowo)}\b', zastepcze_slowo, tekst, flags=re.IGNORECASE)
    return tekst


# przykładowy tekst wejściowy
tekst_wejsciowy1 = "123 xx 322 qwe 234 666 zz 213 777 yy "

tekst_wejsciowy2 = "program do zamiany słów na inne"


# słowa do usunięcia
slowa_do_usuniecia = ["xx", "yy", "zz", "123"]


# Słownik zamiany
slownik_zamiany = {
    'zamiany': 'podmiany',
    'słów': 'wyrazów',
    'inne': 'różne',
}


tekst_po_usunieciu = usun_slowa(tekst_wejsciowy1, slowa_do_usuniecia)
print("Tekst po usunięciu:", tekst_po_usunieciu)


tekst_po_zamianie = zamien_slowa(tekst_wejsciowy2, slownik_zamiany)
print("Tekst po zmianie:", tekst_po_zamianie)



