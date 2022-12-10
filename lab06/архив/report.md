---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе 6"
subtitle: "Разложение чисел на множители"
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

Реализация алгоритма, реализующий p-метод Полларда.
 
# Теоретические сведения

Один из простейших способов разложить число на простые множители − это проверить, делится ли данное число на 2, 3, 5 ,... и т.д., т.е. проверить, делится ли число на ряд простых чисел. Если число n не делится ни на какое простое число до , то даннаое число является простым, т.к. если число составное, то имеет по крайней мере два множителя и оба они не могут быть больше .

Представим алгоритм разложения числа n на простые множители. Подготовим заранее таблицу простых чисел до s=. Обозначим ряд простых чисел через $p_1, p_2, ..., p_k$ [1].


**p-алгоритм Поллрада**

* Вход. Число $n$, начальное значение $c$, функция $f$, обладающая сжимающими свойствами.
* Выход. Нетривиальный делитель числа $n$.

1. Положить $a=c, b=c$
2. Вычислить $a=f(a)(mod n), b=f(b)(mod n)$
3. Найти $d = GCD(a-b, n)$
4. Если $1<d<n$, то положить $p=d$ и результат: $p$. При $d=n$ результат: ДЕЛИТЕЛЬ НЕ НАЙДЕН. При $d=1$ вернуться на шаг 2.



# Выполнение лабораторной работы

1. Написал функцию pollarda для алгоритма полларда. (рис. -@fig:001)

![Функция для алгоритма полларда](image/1.png){ #fig:001 width=70% }


6. Получил результат (рис. -@fig:002)

![Результат алгоритма](image/2.png){ #fig:002 width=70% }

# Выводы

Реализовал алгоритм, реализующий p-метод Полларда.

# Список литературы

1. Разложение числа на простые множители онлайн [Электронный ресурс] - Режим доступа: https://matworld.ru/teorija-chisel/razlozhenie-chisel.php

