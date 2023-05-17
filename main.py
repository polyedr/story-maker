import argparse
from typing import Optional
from positions import list_of_strings_positions
from strings import list_of_strings, stop_words


class TextFormatter:
    def __init__(
        self, strings: list, positions: list, stop_words: Optional[list] = None
    ):
        self.strings = strings
        self.positions = positions
        self.stop_words = stop_words if stop_words else []

    def get_as_list(self, username: str) -> list:
        """
        Метод возвращает правильно сформированный список слов итогового текста.
        Среди возвращаемых элементов не должно содержаться слов из списка стоп-слов.
        Элементы списка, содержащие шаблон {username}, должны быть заменены на значение переменной username.
        :param username: Имя пользователя
        :return: Список слов в правильном порядке
        """
        e_strings = []
        # Linearization of the positions
        flat_positions = []

        for i in self.positions:
            if isinstance(i, list):
                flat_positions.extend(i)
            else:
                flat_positions.append(i)

        # Create an initial dictionary
        dict_strings = dict(zip(self.strings, self.positions))

        # Multiplicating of the strings
        for key, value in dict_strings.items():
            if isinstance(value, int):
                e_strings.append(key)
            else:
                e_strings.extend([key] * len(value))

        # Obtaining the ordered strings
        ordered_strings = [x for _, x in sorted(zip(flat_positions, e_strings))]

        # Username replacement
        ordered_strings = [i.replace("{username}", username) for i in ordered_strings]

        # Move out the stop words
        ordered_strings = [x for x in ordered_strings if x not in self.stop_words]

        self.strings = ordered_strings

        return self.strings

    def get_as_text(self, username: str) -> str:
        """
        Метод возвращает текст, сформированный из списка слов и позиций.
        В возвращаемом тексте не должно быть стоп-слов.
        Шаблон {username} должен быть заменён на значение переменной username.
        Каждое новое предложение должно начинаться с большой буквы.
        Между знаком препинания и впереди стоящим словом не должно быть пробелов.
        :param username: Имя пользователя
        :return: Текст, отформатированный согласно условиям задачи
        """
        ordered_strings = self.get_as_list(username)

        # Capitalize the first word
        ordered_strings[0] = ordered_strings[0].capitalize()

        # Define the delimiters
        delimiters = frozenset({".", "?", "!"})
        delimiters_plus = frozenset({".", "?", "!", ","})

        for i in range(len(ordered_strings) - 1):
            if ordered_strings[i] in delimiters:
                ordered_strings[i + 1] = ordered_strings[i + 1].capitalize()

        # Assemble the strings
        text = ""
        for i in range(len(ordered_strings)):
            if i == 0:
                text += ordered_strings[i]
            elif ordered_strings[i] in delimiters_plus:
                text += ordered_strings[i]
            else:
                text += " "
                text += ordered_strings[i]

        return text


if __name__ == "__main__":
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
        # print(formatter.get_as_list(arguments.username))
