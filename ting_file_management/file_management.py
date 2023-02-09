import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato Invalido\n')
    try:
        with open(path_file) as file:
            file_txt = file.read()
            return file_txt.split('\n')
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
