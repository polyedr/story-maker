## Задача по составлению текста из списков
Для выполнения задачи рекомендуется использовать версию **Python 3.6+**.

#### Запустите тесты

`python -m unittest`

Сейчас тест вернёт только ошибки, однако, если вы выполните задание в точности как описано,
 тест должен показать *зелёный* результат.

#### Реализуйте cli-приложение, которое формирует текст из списка строк и списка позиций 

Конструктор класса принимает три списка:
- Список слов
- Список позиций
- Список стоп-слов

Далее приложение должно составить из предоставленных списков предложения в правильном
порядке, исключив стоп-слова.

**Например:** из списка слов `["раму", "мама", "мыла"]` и списка позиций, `[2,0,1]` должен
получиться упорядоченный список `["мама", "мыла", "раму"]` и предложение `Мама мыла раму`.
Важно обратить внимание, что при составлении предложений класс должен писать с большой буквы
первое слово каждого предложения.

Если слово повторяется несколько раз в тексте, то в списке позиций вместо значения `<int>`
будет содержаться список со всеми позициями, в которых находится слово.

**Например:** из списка слов `["ни", "то", "сё"]` и списка позиций `[[0,2],1,3]` должен
получиться упорядоченный список `["ни", "то", "ни", "cё"]`.

Кроме того, методы класса `get_as_list` и `get_as_text` принимают аргумент `username`, на
значение которого меняют шаблон `{username}`, если такой элемент встречается в списке.

**Например:** из списка слов `["привет", ",", "{username}", "!"]` и списка позиций 
`[0,1,2,3]` при вызове метода `get_as_list` с аргументом **"Alex"** должен получиться
упорядоченный список `["привет", ",", "Alex", "!"]`

При составлении предложений между словани нужно поставить пробелы, за исключением
слов, которые являются знаками препинания. Такие знаки отделяются пробелом только от 
последующего слова, но не от предыдущего.

**Например:** если метод `get_as_list` возвращает список
`["это", ",", "очевидно", ",", "плохо", "."]`, то метод `get_as_text` должен вернуть
такое предложение **"Это, очевидно, плохо."**


#### Запустите программу

```bash
python main.py -u Alex
```

```bash
python main.py --username Alex
```

Вместо **Alex** используйте любое имя.

Результат должен выглядеть следующим образом:
```bash
python main.py --username Alex
Пришло время выслушать невероятную историю, Alex. Это было обычное утро,
ничем не отличавшееся от любого другого, за одним маленьким исключением.
Сегодня утром тебе, Alex, прислали это замечательное задание. И что в нём
замечательного, спросишь ты? Этот текст соберётся автоматически, и это
запрограммируешь ты!
```

#### Обеспечте прохождение кодом тестов
Если всё выполнено согласно требованиям задачи, тесты должны возвращать два успешных
результата.
```bash
python -m unittest
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Все необходимые файлы находятся в папке с проектом.

