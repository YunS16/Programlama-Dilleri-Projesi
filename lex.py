import re 
def kod_parcala(code):
    tokens = []
    anahtar_kelimeler = ["int","if","else","while","return"]
    islemciler =["==","=","+","-","*","/"]
    ayraclar = ["(", ")", "{", "}", ";", ","]


    words = re.findall(r'\w+|==|=|\+|-|\*|/|\(|\)|\{|\}|;|,', code)

    for word in words:
        if word in anahtar_kelimeler:
            tokens.append(("KEYWORDS", word))

        elif word.isdigit():
            tokens.append(("NUMBER", word))
            
        elif word.isidentifier():
            tokens.append(("IDENTIFIER", word))

        elif word in islemciler:
            tokens.append(("OPERATOR", word))
        elif word in ayraclar:
            tokens.append(("DELIMITER", word))
        
        else:
            tokens.append(("UNKNOWN", word))

    return tokens