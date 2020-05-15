from string import ascii_lowercase

alphabet = ascii_lowercase


def act(action_name, cipher_type, key, text):
    if cipher_type == 'caesar':
        key = int(key)
    return cipher_shift(cipher_type, key, text, action_name)


def cipher_shift(cipher, key, text, mode):
    new_text = []
    if cipher == 'caesar':
        additions = [key] if mode == 'encode' else [-key]
    else:
        additions = list(alphabet.index(x) + 1 for x in key) if mode == 'encode' \
            else list(-alphabet.index(x) - 1 for x in key)
    for idx, ch in enumerate(text):
        if ch.lower() not in alphabet:
            new_text.append(ch)
            continue
        cur_alphabet = alphabet.upper() if ch in alphabet.upper() else alphabet
        new_text.append(cur_alphabet[(cur_alphabet.index(ch) + len(cur_alphabet) + additions[idx % len(additions)])
                                     % len(cur_alphabet)])
    return "".join(new_text)
