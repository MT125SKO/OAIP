import cProfile


def count_words(file_path):
    file = open(file_path, 'r')
    content = file.read()
    words = content.split()
    unique_words = {}
    for word in words:
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1
    file.close()
    return unique_words


file_path = "file_path.txt"
cProfile.run(f'count_words("{file_path}")')

##########################################################

import cProfile


def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().lower().split()  #
            unique_words = {}
            for word in words:
                unique_words[word] = unique_words.get(word, 0) + 1
            return unique_words
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return None
    except OSError as e:
        print(f"Ошибка: {e}")
        return None


file_path = "file_path.txt"

cProfile.run(f'count_words("{file_path}")') 