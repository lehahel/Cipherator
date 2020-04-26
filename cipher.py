alphabet_size = 26
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encode(cipher_type, key, text):
    if cipher_type == 'caesar':
        key = int(key)
        return caesar_shift(key, text, 'encode')
    elif cipher_type == 'vigenere':
        return vigenere_shift(key, text, 'encode')


def decode(cipher_type, key, text):
    if cipher_type == 'caesar':
        key = int(key)
        return caesar_shift(key, text, 'decode')
    elif cipher_type == 'vigenere':
        return vigenere_shift(key, text, 'decode')


def caesar_shift(key, text, mode):
    shift = key if mode == 'encode' else -key
    new_text = ""
    for ch in text:
        if ch in upper_alphabet:
            new_text += upper_alphabet[(upper_alphabet.index(ch) + alphabet_size + shift) % alphabet_size]
        elif ch in lower_alphabet:
            new_text += lower_alphabet[(lower_alphabet.index(ch) + alphabet_size + shift) % alphabet_size]
        else:
            new_text += ch
    return new_text


def vigenere_shift(key, text, mode):
    new_text = ""
    additions = list(lower_alphabet.index(x) + 1 for x in key) if mode == 'encode' \
        else list(-lower_alphabet.index(x) - 1 for x in key)
    for i in range(len(text)):
        if text[i] in upper_alphabet:
            new_text += upper_alphabet[(upper_alphabet.index(text[i]) + alphabet_size + additions[i % len(additions)])
                                       % alphabet_size]
        elif ord('a') <= ord(text[i]) <= ord('z'):
            new_text += lower_alphabet[(lower_alphabet.index(text[i]) + alphabet_size + additions[i % len(additions)])
                                       % alphabet_size]
        else:
            text += text[i]
    return new_text
