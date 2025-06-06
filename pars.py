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

def ifade():
    return esles("IDENTIFIER") or esles("NUMBER")

def kosul():
    return esles("IDENTIFIER") and esles("OPERATOR", "==") and esles("NUMBER")

def degisken_tanim():
    return esles("KEYWORDS", "int") and esles("IDENTIFIER") and esles("OPERATOR", "=") and esles("NUMBER") and esles("DELIMITER", ";")

def atama():
    return esles("IDENTIFIER") and esles("OPERATOR", "=") and ifade() and esles("DELIMITER", ";")

def eger_durumu():
    if esles("KEYWORDS", "if") and esles("DELIMITER", "(") and kosul() and esles("DELIMITER", ")") and esles("DELIMITER", "{") and komut() and esles("DELIMITER", "}"):
        return True
    return False

def komut():
    global pos
    yer = pos
    if degisken_tanim() or atama() or eger_durumu():
        return True
    pos = yer
    return False

def program():
    global pos
    while pos < len(tokens):
        if not komut():
            return False
    return True
