pos = 0
tokens = []

def esles(tip, deger=None):
    global pos
    if pos < len(tokens):
        t_tur, t_deger = tokens[pos]
        if t_tur == tip and (deger is None or t_deger == deger):
            pos += 1
            return True
    return False

def program(gelen_tokens):
    global pos, tokens
    tokens = gelen_tokens
    pos = 0
    while pos < len(tokens):
        if not statement():
            return False
    return True

def statement():
    return degisken_tanim() or if_yapisi()

def degisken_tanim():
    global pos
    yer = pos
    if (esles("KEYWORDS", "int") and 
        esles("IDENTIFIER") and 
        esles("OPERATOR", "=") and 
        (esles("NUMBER") or esles("IDENTIFIER")) and 
        esles("DELIMITER", ";")):
        return True
    pos = yer
    return False

def if_yapisi():
    global pos
    yer = pos
    if (esles("KEYWORDS", "if") and
        esles("DELIMITER", "(") and 
        ifade() and 
        esles("DELIMITER", ")")):
        
        # süslü parantezli blok
        if esles("DELIMITER", "{"):
            while not esles("DELIMITER", "}"):
                if not statement():
                    pos = yer
                    return False
            return True
        # süslüsüz tek satır
        elif statement():
            return True

    pos = yer
    return False

def ifade():
    global pos
    yer = pos
    if esles("IDENTIFIER") and esles("OPERATOR", "==") and (esles("NUMBER") or esles("IDENTIFIER")):
        return True
    pos = yer
    return False
