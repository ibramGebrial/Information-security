---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе 7"
subtitle: "Дискретное логарифмирование в конечном поле"
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

Реализация алгоритма, реализующий p-метод Полларда для задач дискретного логарифмирования.
 
# Теоретические сведения

Пусть в некоторой конечной мультипликативной абелевой группе $G$ задано уравнение

$$g^x=a$$

Решение задачи дискретного логарифмирования состоит в нахождении некоторого целого неотрицательного числа $x$, удовлетворяющего уравнению. Если оно разрешимо, у него должно быть хотя бы одно натуральное решение, не превышающее порядок группы.
Это сразу даёт грубую оценку сложности алгоритма поиска решений сверху — алгоритм полного перебора нашёл бы решение за число шагов не выше порядка данной группы.

Чаще всего рассматривается случай, когда группа является циклической, порождённой элементом $g$.
В этом случае уравнение всегда имеет решение. 
В случае же произвольной группы вопрос о разрешимости задачи дискретного логарифмирования, то есть вопрос о существовании решений уравнения , требует отдельного рассмотрения.


**p-алгоритм Поллрада**

* Вход. Простое число $p$, число $a$ порядка $r$ по модулю $p$, целое число $b$ $1 < b < p$; отображение $f$, обладающее сжимающими свойствами и сохраняющее вычислимость логарифма.
* Выход. показатель $x$, для которого $a^x=b(mod p)$, если такой показатель существует.

1. Выбрать произвольные целые числа $u, v$ и положить $c=a^u b^v (mod p), d=c$
2. Выполнять $c=f(c)(mod p), d=f(f(d))(mod p)$, вычисляя при этом логарифмы для $c$ и $d$ как линейные функции от $x$ по модулю $r$, до получения равенства $c=d (mod p)$
3. Приняв логарифмы для $c$ и $d$, вычислить логарифм $x$ решением сравнения по модулю $r$. Результат $x$ или РЕШЕНИЯ НЕТ.


# Выполнение лабораторной работы

1. Написал функцию ext_euclid и inverse (рис. -@fig:001)

![Функция для расширенного алгоритма Евклида и обратного значнения](image/1.png){ #fig:001 width=70% }

2. Написал функцию xab  (рис. -@fig:002)

![Функция xab](image/2.png){ #fig:002 width=70% }


3. Написал функцию pollard (рис. -@fig:003)

![Функция для алгоритма pollard](image/3.png){ #fig:003 width=70% }

4. Написал функцию verify и блок работы программы(рис. -@fig:004)

![Функция verify и блок работы программы](image/4.png){ #fig:004 width=70% }

5. Получил результат (рис. -@fig:005)

![Результат алгоритма](image/5.png){ #fig:005 width=70% }

# Выводы

Реализовал реализующий p-метод Полларда для задач дискретного логарифмирования.

# Список литературы

1. Дискретное логарифмирование [Электронный ресурс] - Режим доступа: https://ru.wikipedia.org/wiki/Дискретное_логарифмирование

