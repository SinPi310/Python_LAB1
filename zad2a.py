
def remove_words(text, words_to_remove):
            for word in words_to_remove:
                text = text.replace(word,"")
            return text


#with open('C:\student\JS_WH Python\LAB1\LAB1', 'r',  encoding='utf-8' ) as file:
    # Odczyt zawartości pliku
#    file_contents = file.read()

#    zmienna = file_contents.split()

#words = ["123", "xx", "322", "qwe", "234", "666", "zz", "213", "777", "yy"]
words = ("123 xx 322 qwe 234 666 zz 213 777 yy ")


if __name__ == '__main__':
    words_to_remove = ["xx", "yy", "zz", "123"]

    result = remove_words(words, words_to_remove)

    print( "Tekst po usunięciu wybranych słów:")
    print(result)


    # print(zmienna)

