def exists_word(word, instance):
    exist_word = []
    list_size = len(instance)

    for _data in range(list_size):
        search_file = instance.search(_data)
        files = {
            "palavra": word,
            "arquivo": search_file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for i, file in enumerate(search_file["linhas_do_arquivo"]):
            if word.lower() in file.lower():
                files["ocorrencias"].append({"linha": i + 1})

        if files["ocorrencias"]:
            exist_word.append(files)

    return exist_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
