---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе 3"
subtitle: "Шифрование гаммированием"
author: "Гебриал Ибрам Есам Зекри НФИ-02-22"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Реализация алгоритма шифрования гаммированием конечной гаммой.

# Теоретические сведения

Гаммирование – метод шифрования, основанный на "наложении" гамма-последовательности на открытый текст. Обычно это суммирование в каком-либо конечном поле (суммирование по модулю). Например, в поле GF(2) такое суммирование принимает вид обычного "исключающего ИЛИ". При расшифровке операция проводится повторно, в результате получается открытый текст.'

В этом способе шифрование выполняется путем сложения символов исходного текста и ключа по модулю, равному числу букв в алфавите. Если в исходном алфавите, например, 33 символа, то сложение производится по модулю 33. Такой процесс сложения исходного текста и ключа называется в криптографии наложением гаммы.

Пусть символам исходного алфавита соответствуют числа от 0 (А) до 32 (Я). Если обозначить число, соответствующее исходному символу, x, а символу ключа – k, то можно записать правило гаммирования следующим образом:

z = x + k (mod N),

где z – закодированный символ, N - количество символов в алфавите, а сложение по модулю N - операция, аналогичная обычному сложению, с тем отличием, что если обычное суммирование дает результат, больший или равный N, то значением суммы считается остаток от деления его на N. Например, пусть сложим по модулю 33 символы Г (3) и Ю (31):

3 + 31 (mod 33) = 1,

то есть в результате получаем символ Б, соответствующий числу 1.

Наиболее часто на практике встречается двоичное гаммирование. При этом используется двоичный алфавит, а сложение производится по модулю два.

Операция сложения по модулю два в алгебре логики называется также "исключающее ИЛИ" или по-английски XOR.

Рассмотрим пример. Предположим, нам необходимо зашифровать десятичное число 14 методом гаммирования с использованием ключа 12. Для этого вначале необходимо преобразовать исходное число и ключ (гамму) в двоичную форму: 14(10)=1110(2), 12(10)=1100(2). Затем надо записать полученные двоичные числа друг под другом и каждую пару символов сложить по модулю два. При сложении двух двоичных знаков получается 0, если исходные двоичные цифры одинаковы, и 1, если цифры разные

Сложим по модулю два двоичные числа 1110 и 1100:

Исходное число 1 1 1 0

Гамма    1 1 0 0

Результат   0 0 1 0

В результате сложения получили двоичное число 0010. Если перевести его в десятичную форму, получим 2. Таким образом, в результате применения к числу 14 операции гаммирования с ключом 12 получаем в результате число 2.

Каким же образом выполняется расшифрование? Зашифрованное число 2 представляется в двоичном виде и снова производится сложение по модулю 2 с ключом:

Зашифрованное число 0 0 1 0

Гамма     1 1 0 0

Результат    1 1 1 0

Переведем полученное двоичное значение 1110 в десятичный вид и получим 14, то есть исходное число.

Таким образом, при гаммировании по модулю 2 нужно использовать одну и ту же операцию как для зашифрования, так и для расшифрования. Это позволяет использовать один и тот же алгоритм, а соответственно и одну и ту же программу при программной реализации, как для шифрования, так и для расшифрования.

Операция сложения по модулю два очень быстро выполняется на компьютере (в отличие от многих других арифметических операций), поэтому наложение гаммы даже на очень большой открытый текст выполняется практически мгновенно.

Благодаря указанным достоинствам метод гаммирования широко применяется в современных технических системах сам по себе, а также как элемент комбинированных алгоритмов шифрования.

Сформулируем, как производится гаммирование по модулю 2 в общем случае:

- символы исходного текста и гамма представляются в двоичном коде и располагаются один под другим, при этом ключ (гамма) записывается столько раз, сколько потребуется;
- каждая пара двоичных знаков складывается по модулю два;
- полученная последовательность двоичных знаков кодируется символами алфавита в соответствии с выбранным кодом.

На (рис. -@fig:001) показано, как применяется гаммирование к тексту с русскими символами. Символы кодируются в соответствии с принятой кодировкой, а затем производится сложение по модулю 2.

При использовании метода гаммирования ключом является последовательность, с которой производится сложение – гамма. Если гамма короче, чем сообщение, предназначенное для зашифрования, гамма повторяется требуемое число раз. Так в примере на рис. 2.6 длина исходного сообщения равна двенадцати байтам, а длина ключа – пяти байтам. Следовательно, для зашифрования гамма должна быть повторена 2 раза полностью и еще один раз частично[1].

![Механизм гаммирования](image/11.jpg){ #fig:001 width=70% }

При использовании генератора ПСП получаем бесконечную гамму. Однако, возможен режим шифрования конечной гаммы. В роли конечной гаммы может выступать фраза. Как и ранее, используется алфавитный порядок букв, т.е. буква «а» имеет порядковый номер 1, «б» - 2 и т.д.

Например, зашифруем слово «ПРИКАЗ» («17 18 10 12 01 09») гаммой «ГАММА» («04 01 14 14 01»). Будем использовать операцию побитового сложения по модулю 33 (mod33).  Получаем:

с1 = 17 + 4(mod33) = 21,	с4=12+ 14(mod33) = 26

с2 = 18 + 1(mod33) = 19,	с5 = 1 + 1(mod33) = 2

с3 = 10 + 14 (mod33) = 24,	с6 = 9 + 4(mod33) = 13.

Криптограмма. «УСЦШБЛ» («20 18 22 24 02 12»).


# Выполнение лабораторной работы

1. Написал функцию gama для шифрования гаммированием конечной гаммой. (рис. -@fig:002)

Сначала написал алфавит в виде списки.

Потом определил индекс каждой буквы в сообщении, аналогично ключу. 

Как определил позицию, сложил на него позиции ключа. потом распечатал зашифрованный текст.

![Функция для кодирования текста шифром гаммированием конечной гаммой](image/1.png){ #fig:002 width=70% }

Получил результат. (рис. -@fig:003)

![Получение шифрования текста методом гаммированием конечной гаммой](image/2.png){ #fig:003 width=70% }

2. Написал функцию для расшировки гаммированием конечной гаммой. (рис. -@fig:004)

Сначала написал алфавит в виде списки.

Потом определил индекс каждой буквы в сообщении, аналогично ключу. 

Как определил позицию, вычитил из него позиции ключа. потом распечатал расшириовки текст.

![Функция для расшифровки текста шифром гаммированием конечной гаммой](image/3.png){ #fig:004 width=70% }

Получил результат. (рис. -@fig:005)

![Получение расшифровки текста методом гаммированием конечной гаммой](image/4.png){ #fig:005 width=70% }

# Выводы

Реализовал алгоритм шифрования гаммированием конечной гаммой.

# Список литературы

1. Методы гаммирования [Электронный ресурс] - Режим доступа: https://www.intuit.ru/stud

ies/courses/691/547/lecture/12373?page=4. - Дата обращения: 05.04.2019.