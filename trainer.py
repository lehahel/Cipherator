import cipher
import json


def hack(text, cipher_type, model_file):
    if cipher_type == 'caesar':
        return caesar_hack(text, model_file)
    else:
        raise NameError('Wrong cipher name')


def get_stat(text):
    stat = [0 for i in range(cipher.alphabet_size)]
    full_sum = 0
    for x in text:
        if x in cipher.lower_alphabet:
            stat[cipher.lower_alphabet.index(x)] += 1
            full_sum += 1
    stat = [x / full_sum for x in stat]
    return stat


def find_model_distance(stat1, stat2):
    if len(stat1) != cipher.alphabet_size or len(stat2) != cipher.alphabet_size:
        raise Exception('Wrong stat')
    distance = 0
    for i in range(cipher.alphabet_size):
        distance += abs(stat1[i] - stat2[i])
    return distance


def shift(stat, value):
    if len(stat) != cipher.alphabet_size:
        raise NameError('Wrong stat')
    new_stat = [0 for i in range(cipher.alphabet_size)]
    first_el = stat[0]
    for i in range(cipher.alphabet_size):
        num = (i + value) % cipher.alphabet_size
        new_stat[i] = stat[num] if num != 0 else first_el
    return new_stat


def caesar_hack(text, model_file):
    my_stat = get_stat(text)
    with open(model_file, "r") as f:
        true_stat = json.load(f)
    best_k = 0
    best_distance = -1
    for k in range(1, cipher.alphabet_size):
        shifted_stat = shift(my_stat, k)
        distance = find_model_distance(shifted_stat, true_stat)
        if distance < best_distance or best_distance == -1:
            best_distance = distance
            best_k = k
    return cipher.act('decode', 'caesar', best_k, text)


def read_stat_file(filename):
    if not isinstance(filename, str):
        raise TypeError('filename should be str')
    stat = []
    with open(filename, 'r') as f:
        for i in range(cipher.alphabet_size):
            stat.append(float(f.readline().strip('\n')))
    return stat


def train(text, model_file):
    stat = get_stat(text)
    with open(model_file, "w") as f:
        json.dump(stat, f)
