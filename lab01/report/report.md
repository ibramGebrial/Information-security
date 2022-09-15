---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе 1"
subtitle: "Шифры простой замены"
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

Приобретение навыков программной реализации простых шифров подстановки и замены.

# Теоретические сведения

Шифр Цезаря (также он является шифром простой замены) - это моноалфавитная подстановка, т.е. каждой букве открытого текста ставится в соответствие одна буква шифртекста. На практике при создании шифра простой замены в качестве шифроалфавита берется исходный алфавит, но с нарушенным порядком букв алфавитная перестановка).

При достижении конца алфавита выполнялся циклический переход к его началу. Таким образом, шифр-алфавит циклически сдвинут влево на K позиций относительно нормативного алфавита.

Цезарь использовал этот шифр замены при смещении. k = 3. Такой шифр можно задать таблицей подстановок, содержащей соответствующие пары букв открытого текста и шифротекста [1]. (рис. -@fig:001)

![Шифр Цезаря ](image/6.png){ #fig:001 width=70% }

Шифр Атбаш:

Еще один шифр простой (моноалфавитной) замены. Шифрование осуществляется путем замены первой буквы алфавита на последнюю, второй на предпоследнюю и так далее. (рис. -@fig:002)

Этот шифр использовался для еврейского алфавита и отсюда получил свое название. Первая буква - алеф, заменяется на тау (последнюю), вторая буква - бет, заменяется на шин (предпоследнюю). Из этих букв и сформировалось название. []

![Шифр Атбаш](image/7.png){ #fig:002 width=70% }



# Выполнение лабораторной работы


1. Написал функцию caesar для шифрования и расшифровки текста. (рис. -@fig:003)

Сначала написал алфавит в виде списки.

Для расшифровки умножил ключ на -1. 

Написал цикл для проверки каждой буквы в нашем слове, а затем определил ее позицию в алфавите с помощью index метода, который возвращает индекс указанного элемента в списке. Как определил позицию, сложил на него ключ (shift). потом распечатал зашифрованный текст.

![Функция для кодирования текста шифром Цезаря](image/1.png){ #fig:003 width=70% }

2. Написал функцию atbash для шифрования и расшифровки текста. (рис. -@fig:004)

Для атбаша сделал аналогично, для сдвига на всю длину алфавита нам нужно умножить позицию на -1.

![Функция для кодирования текста шифром Атбаша](image/2.png){ #fig:004 width=70% }


3. Написал блок выбора нужного метода и ввода текста. (рис. -@fig:005)


![Код для выбора метод шифрования и ввода текста](image/3.png){ #fig:005 width=60% }

4. Зашифровал и расшифровал слова Hello с помощью шифра Цезаря. (рис. -@fig:006)

![Получение шифрования и расшифровки текста методом Цезаря ](image/4.png){ #fig:006 width=70% }


5. Зашифровал и расшифровал слова Hello с помощью Атбаша. (рис. -@fig:007)

![Получение шифрования текста методом Атбаша](image/5.png){ #fig:007 width=70% }



# Выводы

Приобрел навыки программной реализации простых шифров подстановки и замены.

# Список литературы

1. Шифры простой замены. — URL: https://studme.org/239550/

informatika/shifry_prostoy_zameny.

2. Шифр Атбаш. — URL: https://studbooks.net/2215784/informatika/shifr_atbash. 