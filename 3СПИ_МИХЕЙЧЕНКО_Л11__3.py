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

#######################################
import cProfile
import mmap
from collections import Counter


def count_words_mmap(file_path):
    try:
        with open(file_path, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0) as mm:
                words = mm.read().decode('utf-8', errors='ignore').lower().split()
                return dict(Counter(words))
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return None
    except OSError as e:
        print(f"Ошибка: {e}")
        return None
    except UnicodeDecodeError:
        print("Ошибка")
        return None


file_path = "file_path.txt"

cProfile.run(f'count_words_mmap("{file_path}")')

