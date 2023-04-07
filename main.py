import argparse

from typing import Optional

from positions import list_of_strings_positions
from strings import list_of_strings, stop_words
from itertools import repeat


class TextFormatter:
    def __init__(
        self, strings: list, positions: list, stop_words: Optional[list] = None
    ):
        self.strings = strings
        # self.filtered_strings = []
        self.positions = positions
        self.stop_words = stop_words if stop_words else []

    def get_as_list(self, username: str) -> list:
        e_strings = []
        # Linearization of the positions
        flat_positions = [item for sublist in self.positions for item in sublist]
        # Create an initial dictionary
        dict_strings = dict(zip(self.strings, self.positions))
        # Multiplicating of the strings
        for key, value in dict_strings:
            if len(value) == 1:
                e_strings.append(key)
            else:
                e_strings.extend(repeat(key, len(value)))

        # Obtaining the ordered strings
        ordered_strings = [x for _, x in sorted(zip(flat_positions, e_strings))]
        # Username replacement
        ordered_strings = [
            i.replace("{username}", arguments.username) for i in ordered_strings
        ]
        # Move out the stop words
        ordered_strings = [x for x in ordered_strings if x not in self.stop_words]

        self.filtered_strings = ordered_strings
        self.strings = ordered_strings
        """
        Метод возвращает правильно сформированный список слов итогового текста.
        Среди возвращаемых элементов не должно содержаться слов из списка стоп-слов.
        Элементы списка, содержащие шаблон {username}, должны быть заменены на значение переменной username.
        :param username: Имя пользователя
        :return: Список слов в правильном порядке
        """
        return self.strings

    def get_as_text(self, username: str) -> str:
        ordered_strings = [
            i.replace("{username}", arguments.username) for i in self.strings
        ]
        ordered_strings = [x for x in ordered_strings if x not in self.stop_words]
        text = " ".join(ordered_strings)
        sentences = ". ".join(
            list(map(lambda x: x.strip().capitalize(), text.split(".")))
        )
        """
        Метод возвращает текст, сформированный из списка слов и позиций.
        В возвращаемом тексте не должно быть стоп-слов.
        Шаблон {username} должен быть заменён на значение переменной username.
        Каждое новое предложение должно начинаться с большой буквы.
        Между знаком препинания и впереди стоящим словом не должно быть пробелов.
        :param username: Имя пользователя
        :return: Текст, отформатированный согласно условиям задачи
        """
        return sentences


formatter = TextFormatter(list_of_strings, list_of_strings_positions, stop_words)

arguments_parser = argparse.ArgumentParser(
    prog="python main.py", description="Консольный рассказчик."
)
arguments_parser.add_argument(
    "-u", "--username", action="store", help="Имя пользователя в истории"
)

arguments = arguments_parser.parse_args()

if arguments.username:
    print(formatter.get_as_text(arguments.username))
