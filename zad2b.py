def zamien_slowa(tekst, zamiana):

    slowa = tekst.split()
    nowy_tekst = []

    for slowo in slowa:
        if slowo in zamiana:
            nowy_tekst.append(zamiana[slowo])
        else:
            nowy_tekst.append(slowo)

    return ' '.join(nowy_tekst)  # Połącz słowa z powrotem w jeden tekst

# Przykładowy słownik zamiany
slownik_zamiany = {
    'zamiany': 'podmiany',
    'słów': 'wyrazów',
    'inne': 'różne',
}

# Przykładowy tekst wejściowy
tekst_wejsciowy = "program do zamiany słów na inne"

# Wywołaj funkcję do zamiany słów
tekst_po_zamianie = zamien_slowa(tekst_wejsciowy, slownik_zamiany)

# Wyświetl zmieniony tekst
print(tekst_po_zamianie)
