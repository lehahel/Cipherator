import cipher
import json

alphabet = cipher.alphabet


def hack(text, cipher_type, model_file):
    if cipher_type == 'caesar':
        return caesar_hack(text, model_file)
    else:
        raise ValueError('Wrong cipher name')


def get_stat(text):
    stat = [0 for i in range(len(alphabet))]
    full_sum = 0
    for x in text:
        if x in alphabet:
            stat[alphabet.index(x)] += 1
            full_sum += 1
    stat = [x / full_sum for x in stat]
    return stat


def find_model_distance(shift, stat1, stat2):
    if len(stat1) != len(alphabet) or len(stat2) != len(alphabet):
        raise ValueError('Wrong stat')
    distance = 0
    for i in range(len(alphabet)):
        distance += abs(shifted(i, stat1, shift) - stat2[i])
    return distance


def shifted(value, stat, k):
    return stat[(value + k) % len(stat)]


def caesar_hack(text, model_file):
    my_stat = get_stat(text)
    with open(model_file, "r") as f:
        true_stat = json.load(f)
    best_k = 0
    best_distance = -1
    for k in range(1, len(alphabet)):
        distance = find_model_distance(k, my_stat, true_stat)
        if distance < best_distance or best_distance == -1:
            best_distance = distance
            best_k = k
    return cipher.act('decode', 'caesar', best_k, text)


def read_stat_file(filename):
    if not isinstance(filename, str):
        raise TypeError('filename should be str')
    stat = []
    with open(filename, 'r') as f:
        for i in range(len(alphabet)):
            stat.append(float(f.readline().strip('\n')))
    return stat


def train(text, model_file):
    stat = get_stat(text)
    with open(model_file, "w") as f:
        json.dump(stat, f)
