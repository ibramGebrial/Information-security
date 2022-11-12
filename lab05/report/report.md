---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе 5"
subtitle: "Вероятностные алгоритмы проверки чисел на простоту"
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

Реализация алгоритмов Ферма,Соловэя-Штрассена, Миллера-Рабина и вычисления Якоби.
 
# Теоретические сведения

Тестом простоты (или проверкой простоты) называется алгоритм, который, приняв на входе число N, позволяет либо не подтвердить предположение о составности числа, либо точно утверждать его простоту. Во втором случае он называется истинным тестом простоты. Таким образом, тест простоты представляет собой только гипотезу о том, что если алгоритм не подтвердил предположение о составности числа N, то это число может являться простым с определённой вероятностью. Это определение подразумевает меньшую уверенность в соответствии результата проверки истинному положению вещей, нежели истинное испытание на простоту, которое даёт математически подтверждённый результат[1].

## Тест Ферма

* Вход. Нечетное целое число $n \geq 5$.
* Выход. «Число n, вероятно, простое» или «Число n составное».

1. Выбрать случайное целое число $a, 2 \leq a \leq n-2$.
2. Вычислить $r=a^{n-1} (mod n)$
3. При $r=1$ результат: «Число n, вероятно, простое». В противном случае результат: «Число n составное» [2].

## Тест Соловэя-Штрассена

* Вход. Нечетное целое число $n \geq 5$.
* Выход. «Число n, вероятно, простое» или «Число n составное».

1. Выбрать случайное целое число $a, 2 \leq a \leq n-2$.
2. Вычислить $r=a^{(\frac{n-1}{2})} (mod n)$
3. При $r \neq 1$ и $r \neq n-1$ результат: «Число n составное».
4. Вычислить символ Якоби $s = (\frac{a}{n})$
5. При $r=s (mod n)$ результат: «Число n, вероятно, простое». В противном случае результат: «Число n составное» [3].

## Тест Миллера-Рабина.

* Вход. Нечетное целое число $n \geq 5$.
* Выход. «Число n, вероятно, простое» или «Число n составное».

1. Представить $n-1$ в виде $n-1 = 2^sr$, где r - нечетное число
2. Выбрать случайное целое число $a, 2 \leq a \leq n-2$.
3. Вычислить $y=a^r (mod n)$
4. При $y \neq 1$ и $y \neq n-1$ выполнить действия
	- Положить $j=1$
	- Если $j \leq s-1$ и $y \neq n-1$ то
		* Положить $y=y^2 (mod n)$
		* При $y=1$   результат: «Число n составное».
		* Положить $j=j+1$
	- При $y \neq n-1$ результат: «Число n составное».
5. Результат: «Число n, вероятно, простое» [4].

# Выполнение лабораторной работы

1. Написал функцию ferma для алгоритма ферма. (рис. -@fig:001)

![Функция для алгоритма ферма](image/1.png){ #fig:001 width=70% }

2. Написал функцию modul для вычисления бинарного эксп. (рис. -@fig:002)

![Функция для вычисления бинарного эксп](image/2.png){ #fig:002 width=70% }

3. Написал функцию jacobian для вычисления Якоби. (рис. -@fig:003)

![Функция для вычисления Якоби](image/3.png){ #fig:003 width=70% }

4. Написал функцию solovoy для алгоритма Соловэя-Штрассена. (рис. -@fig:004)

![Функция для алгоритма Соловэя-Штрассена](image/4.png){ #fig:004 width=70% }

5. Написал функцию MillerRabin для алгоритма Миллера-Рабина. (рис. -@fig:005)

![Функция для алгоритма Миллера-Рабина](image/5.png){ #fig:005 width=70% }

6. Получил результат (рис. -@fig:006)

![Результат алгоритмов](image/6.png){ #fig:006 width=70% }

# Выводы

Реализовал алгоритмы Ферма,Соловэя-Штрассена, Миллера-Рабина и вычисления Якоби.

# Список литературы

1. Тест простоты [Электронный ресурс] - Режим доступа: https://ru.wikipedia.org/wiki/Тест_простоты

2. Тест Ферма [Электронный ресурс] - Режим доступа: https://ru.wikipedia.org/wiki/Тест_Ферма

3. Тест Соловея — Штрассена [Электронный ресурс] - Режим доступа: https://ru.wikipedia.org/wiki/Тест_Соловея_—_Штрассена

4. Тест Миллера — Рабина [Электронный ресурс] - Режим доступа: https://ru.wikipedia.org/wiki/Тест_Миллера_—_Рабина