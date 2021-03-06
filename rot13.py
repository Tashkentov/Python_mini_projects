def rot13(message):
    r13code = ""
    rot13_crypt = { 'a': 'n', 'n':'a',
                    'b': 'o', 'o': 'b',
                    'c': 'p', 'p': 'c',
                    'd': 'q', 'q': 'd',
                    'e': 'r', 'r': 'e',
                    'f': 's', 's': 'f',
                    'g': 't', 't': 'g',
                    'h': 'u', 'u': 'h',
                    'i': 'v', 'v': 'i',
                    'j': 'w', 'w': 'j',
                    'k': 'x', 'x': 'k',
                    'l': 'y', 'y': 'l',
                    'm': 'z', 'z': 'm'}
    encrypt = list(message)
    for i in encrypt:
        if i.isupper():
            r13code += rot13_crypt[i.lower()].upper()
        elif i not in rot13_crypt:
            r13code += i
        else:
            r13code += rot13_crypt[i]
    return r13code

print(rot13("v nz grf(ybir) zhfgnpur!"))
