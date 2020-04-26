def read_text(filename=None):
    if filename is None:
        return input()
    with open(filename, 'r') as f:
        return f.read()


def write_text(text, filename=None):
    if filename is None:
        print(text)
    else:
        with open(filename, 'w') as f:
            f.write(text)
