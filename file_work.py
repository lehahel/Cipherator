def read_text(filename=None):
    if filename is None:
        res = ''
        new_str = input()
        while new_str:
            res += '\n' + new_str
            new_str = input()
        return res

    with open(filename, 'r') as f:
        return f.read()


def write_text(text, filename=None):
    if filename is None:
        print(text)
    else:
        with open(filename, 'w') as f:
            f.write(text)
