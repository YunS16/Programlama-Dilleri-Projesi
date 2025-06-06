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

def program(gelen_tokens):
    global pos, tokens
    tokens = gelen_tokens
    pos = 0
    return degisken_tanim() and pos == len(tokens)
