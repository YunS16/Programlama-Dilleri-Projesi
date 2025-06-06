import re

def kod_parcala(code):
    tokens = []
    words = re.findall(r'\bint\b|\bif\b|\d+|[a-zA-Z_]\w*|==|=|\+|-|\*|/|\(|\)|\{|\}|;|,', code)
    
    for word in words:
        if word in ["int", "if", "else", "while", "return"]:
            tokens.append(("KEYWORDS", word))
        elif word.isdigit():
            tokens.append(("NUMBER", word))
        elif word in ["=", "+", "-", "*", "/", "=="]:
            tokens.append(("OPERATOR", word))
        elif word in ["(", ")", "{", "}", ";", ","]:
            tokens.append(("DELIMITER", word))
        elif word.isidentifier():
            tokens.append(("IDENTIFIER", word))
    
    return tokens
