INVALID_SYMBOLS = ['"', ',', '।', ';', '-', "'", '[', ']', '?', '!', '(', ')']

def get_match(file, suffix):
    result = []
    f = open(file, "r", encoding="utf8")
    tokens = []
    for line in f.readlines():
        tokens.extend(line.strip().split(" "))
    for symbol in INVALID_SYMBOLS:
        tokens = [word.replace(symbol, '') for word in tokens]
    for token in set(tokens):
        if token[-len(suffix):] == suffix:
            result.append(token)
    return result

def get_all(file):
    f = open(file, "r", encoding="utf8")
    tokens = []
    for line in f.readlines():
        tokens.extend(line.strip().split(" "))
    for symbol in INVALID_SYMBOLS:
        tokens = [word.replace(symbol, '') for word in tokens if len(word) > 1]
    return set(tokens)
