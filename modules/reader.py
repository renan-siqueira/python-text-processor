def read_from_file(filename):
    """Lê o conteúdo de um arquivo e retorna como uma string."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def write_to_file(filename, content):
    """Escreve o conteúdo fornecido em um arquivo."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
