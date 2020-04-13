def get_file_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def write_res(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
