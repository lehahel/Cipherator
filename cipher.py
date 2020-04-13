def encode(cipher_type, key, text):
    if cipher_type == 'caesar':
        return caesar_encode(key, text)
    elif cipher_type == 'vigenere':
        return vigenere_encode(key, text)


def decode(cipher_type, key, text):
    if cipher_type == 'caesar':
        return caesar_decode(key, text)
    elif cipher_type == 'vigenere':
        return vigenere_decode(key, text)


def caesar_encode(key, text):
    new_text = ""
    alphabet_sz = 26
    for ch in text:
        if ord('A') <= ord(ch) <= ord('Z'):
            new_text += chr((ord(ch) - ord('A') + key) % alphabet_sz + ord('A'))
        elif ord('a') <= ord(ch) <= ord('z'):
            new_text += chr((ord(ch) - ord('a') + key) % alphabet_sz + ord('a'))
        else:
            new_text += ch
    return new_text


def caesar_decode(key, text):
    new_text = ""
    alphabet_sz = 26
    for ch in text:
        if ord('A') <= ord(ch) <= ord('Z'):
            new_text += chr((ord(ch) - ord('A') + alphabet_sz - key) % alphabet_sz + ord('A'))
        elif ord('a') <= ord(ch) <= ord('z'):
            new_text += chr((ord(ch) - ord('a') + alphabet_sz - key) % alphabet_sz + ord('a'))
        else:
            new_text += ch
    return new_text


def vigenere_encode(key, text):
    new_text = ""
    additions = list(ord(x) - ord('a') for x in key)
    alphabet_sz = 26
    for i in range(len(text)):
        if ord('A') <= ord(text[i]) <= ord('Z'):
            new_text += chr((ord(text[i]) - ord('A') + additions[i % len(additions)]) % alphabet_sz + ord('A'))
        elif ord('a') <= ord(text[i]) <= ord('z'):
            new_text += chr((ord(text[i]) - ord('a') + additions[i % len(additions)]) % alphabet_sz + ord('a'))
        else:
            text += text[i]
    return new_text


def vigenere_decode(key, text):
    new_text = ""
    additions = list(ord(x) - ord('a') for x in key)
    alphabet_sz = 26
    for i in range(len(text)):
        if ord('A') <= ord(text[i]) <= ord('Z'):
            new_text += chr((ord(text[i]) - ord('A') + alphabet_sz - additions[i % len(additions)])
                            % alphabet_sz + ord('A'))
        elif ord('a') <= ord(text[i]) <= ord('z'):
            new_text += chr((ord(text[i]) - ord('a') + alphabet_sz - additions[i % len(additions)])
                            % alphabet_sz + ord('a'))
        else:
            text += text[i]
    return new_text

