from .file_management import txt_importer
import sys


def process(path_file, instance):
    file_data = txt_importer(path_file)
    len_file = len(instance)

    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_data),
            "linhas_do_arquivo": file_data
        }

    if len_file > 0:
        for file in instance.queue:
            if file['nome_do_arquivo'] == path_file:
                return None

    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write('Não há elementos\n')
    file = instance.dequeue()
    message = f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n"
    sys.stdout.write(message)


def file_metadata(instance, position):
    if position >= len(instance):
        return sys.stderr.write('Posição inválida')
    search = instance.search(position)
    sys.stdout.write(str(search) + '\n')
