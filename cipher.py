from string import ascii_lowercase

alphabet = ascii_lowercase


def act(action_name, cipher_type, key, text):
    if cipher_type == 'caesar':
        key = int(key)
        return caesar_shift(key, text, action_name)
    elif cipher_type == 'vigenere':
        return vigenere_shift(key, text, action_name)


def caesar_shift(key, text, mode):
    shift = key if mode == 'encode' else -key
    new_text = []
    for ch in text:
        if ch not in alphabet and ch not in alphabet.upper():
            new_text.append(ch)
            continue
        cur_alphabet = alphabet.upper() if ch in alphabet.upper() else alphabet
        new_text.append(cur_alphabet[(cur_alphabet.index(ch) + len(cur_alphabet) + shift) % len(cur_alphabet)])
    return "".join(new_text)


def vigenere_shift(key, text, mode):
    new_text = []
    additions = list(alphabet.index(x) + 1 for x in key) if mode == 'encode' \
        else list(-alphabet.index(x) - 1 for x in key)
    for i in range(len(text)):
        if text[i] not in alphabet and text[i] not in alphabet.upper():
            new_text.append(text[i])
            continue
        cur_alphabet = alphabet.upper() if text[i] in alphabet.upper() else alphabet
        new_text.append(cur_alphabet[(cur_alphabet.index(text[i]) + len(cur_alphabet) + additions[i % len(additions)])
                                     % len(cur_alphabet)])
    return "".join(new_text)
