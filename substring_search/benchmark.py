from boyer_moore import boyer_moore_search
from rabin_karp import rabin_karp_search
from kmp import kmp_search

import timeit


# function to load file as string
def load_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def mean(lst):
    return sum(lst) / float(len(lst))


def benchmark(source_file, strings_to_find):
    setup_code = f"text = load_file('{source_file}')"

    algorithms = {
        "Boyer-Moore": "boyer_moore_search",
        "Rabin-Karp": "rabin_karp_search",
        "Knuth–Morris–Pratt": "kmp_search"
    }

    for algorithm, func_name in algorithms.items():
        print(f"\n{algorithm}:\n")

        for name, string_to_find in strings_to_find.items():
            print(f"{name}:")
            test_code = f"{func_name}(text, \"{string_to_find}\")"
            print(f"{mean(timeit.repeat(test_code, setup=setup_code, globals=globals(), number=20, repeat=20)):.4f} s")


def main():
    print("\nArticle 1\n")

    strings_to_find = {
        "word in the begining of a text": "програмна",
        "word in the middle of a text": "розподілених",
        "word in the end of a text": "wikipedia",
        "word not presented in a text": "абракадабра",
        "phrase in the beginning of a text": "історію комп'ютерних наук",
        "phrase in the middle of a text": "розкривається відміна алгоритму",
        "phrase in the end of a text": "інструмент досягнення мети",
        "phrase not presented in a text": "сонячний день, весняна свіжість",
        "sentence in the beginning of a text": "Алгоритми – це послідовність точно визначених дій, які призводять до вирішення поставленої задачі чи певного завдання",
        "sentence in the middle of a text": "Інтерполяційний пошук використовується для пошуку елементів у відсортованому масиві",
        "sentence in the end of a text": "Правильно підібраний алгоритм пошуку, що враховує ці обмеження відіграє визначальну роль у продуктивності системи",
        "sentence not presented in a text": "Із запашним ароматом свіжої кави в руках, дивлячись на весняний ранок, коли трави вже встигли оновитися під променями сонця, відчуваєш неповторну гармонію природи"
    }

    benchmark('./test_data/article_1.txt', strings_to_find)

    print("\n\nArticle 2\n")

    strings_to_find = {
        "word in the begining of a text": "дослідження",
        "word in the middle of a text": "відфільтрувати",
        "word in the end of a text": "безмасштабных",
        "word not presented in a text": "абракадабра",
        "phrase in the beginning of a text": "структур даних для побудови",
        "phrase in the middle of a text": "для порівняння часу формування",
        "phrase in the end of a text": "найкращі показники швидкодії",
        "phrase not presented in a text": "сонячний день, весняна свіжість",
        "sentence in the beginning of a text": "Метою даної роботи є дослідження та програмна реалізація методів і структур даних для побудови бази даних",
        "sentence in the middle of a text": "Було проведено 4 серії експериментів. Нижче наведено параметри кожної серії",
        "sentence in the end of a text": "Відповідно до результатів проведених експериментів, розгорнутий список показав найкращі показники швидкодії",
        "sentence not presented in a text": "Із запашним ароматом свіжої кави в руках, дивлячись на весняний ранок, коли трави вже встигли оновитися під променями сонця, відчуваєш неповторну гармонію природи"
    }

    benchmark('./test_data/article_2.txt', strings_to_find)


if __name__ == '__main__':
    main()
