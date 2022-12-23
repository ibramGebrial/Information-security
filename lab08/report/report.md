---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе 8"
subtitle: "Целочисленная арифметика многократной точности"
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

Ознакомление с алгоритмами целочисленной арифметики многократной точности, а также их последующая программная реализация.
 
# Теоретические сведения

Высокоточная (длинная) арифметика — это операции (базовые арифметические действия, 
элементарные математические функции и пр.) над числами большой разрядности 
(многоразрядными числами), т.е. числами, разрядность которых превышает 
длину машинного слова универсальных процессоров общего назначения (более 128 бит).

В современных асимметричных криптосистемах в качестве ключей, как правило, 
используются целые числа длиной 1000 и более битов. 
Для задания чисел такого размера не подходит ни один стандартный целочисленный 
тип данных современных языков программирования. Представление чисел в формате 
с плавающей точкой позволяет задать очень большие числа 
(например, тип long double языка C++ -- до $10^{5000}$), 
но не удовлетворяет требованию абсолютной точности, 
характерному для криптографических приложений. Поэтому большие целые числа 
представляются в криптографических пакетах в виде последовательности цифр 
в некоторой системе счисления (обозначим основание системы счисления $b$): $x = (x_{n-1} x_{n-2} \ldots x_1 x_0)_b,$ где $\forall i \in [0, n - 1]: 0 \le x_i < b$.

Основание системы счисления $b$ выбирается так, чтобы существовали машинные команды 
для работы с однозначными и двузначными числами; как правило, $b$ равно $2^8$, $2^{16}$ или $2^{32}$.

При работе с большими целыми числами знак такого числа удобно хранить 
в отдельной переменной. Например, при умножении двух чисел знак произведения вычисляется отдельно.

Далее при описании алгоритмов квадратные скобки означают, что берётся целая часть числа.

## Сложение неотрицательных целых чисел

*Вход. Два неотрицательных числа $u = u_1 u_2 \ldots u_n$ и $v = v_1 v_2 \ldots v_n$; разрядность чисел $n$; основание системы счисления $b$.

*Выход. Сумма $w = w_0 w_1 \ldots w_n$, где $w_0$ - цифра переноса, всегда равная $0$ либо $1$.

1. Присвоить $j = n, k = 0$ (*$j$ идет по разрядам, $k$ следит за переносом*).
2. Присвоить $w_j = (u_j + v_j + k) \pmod{b}$, где $k = \left[ \frac{u_j + v_j + k}{b} \right]$.
3. Присвоить $j = j - 1$. Если $j > 0$, то возвращаемся на шаг 2; если $j = 0$, то присвоить $w_0 = k$ и результат: $w$.

## Вычитание неотрицательных целых чисел

*Вход. Два неотрицательных числа $u = u_1 u_2 \ldots u_n$ и $v = v_1 v_2 \ldots v_n$, $u > v$; разрядность чисел $n$; основание системы счисления $b$.

*Выход. Разность $w = w_0 w_1 \ldots w_n = u - v$.

1. Присвоить $j = n, k = 0$ ($k$ -- заём из старшего разряда).
2. Присвоить $w_j = (u_j - v_j + k) \pmod{b}$; $k = \left[ \frac{u_j - v_j + k}{b} \right]$.
3. Присвоить $j = j - 1$. Если $j > 0$, то возвращаемся на шаг 2; если $j = 0$, то результат: $w$.

## Умножение неотрицательных целых чисел столбиком

*Вход. Числа $u = u_1 u_2 \ldots u_n$, $v = v_1 v_2 \ldots v_m$; основание системы счисления $b$.

*Выход. Произведение $w = uv = w_1 w_2 \ldots w_{m+n}$.

1. Выполнить присвоения: $w_{m+1} = 0, w_{m+2} = 0, \ldots, w_{m+n} = 0, j = m$ (*$j$ перемещается по номерам разрядов числа $v$ от младших к старшим*).
2. Если $v_j = 0$, то присвоить $w_j = 0$ и перейти на шаг 6.
3. Присвоить $i = n, k = 0$ (*значение $i$ идет по номерам разрядов числа $u$, $k$ отвечает за перенос*).
4. Присвоить $t = u_i \cdot v_j + w_{i+j} + k, w_{i+j} = t \pmod{b}, k = \left[ \frac{t}{b} \right]$.
5. Присвоить $i = i - 1$. Если $i > 0$, то возвращаемся на шаг 4, иначе присвоить $w_j = k$.
6. Присвоить $j = j - 1$. Если $j > 0$, то вернуться на шаг 2. Если $j = 0$, то результат: $w$.

## Быстрый столбик

*Вход. Числа $u = u_1 u_2 \ldots u_n$, $v = v_1 v_2 \ldots v_m$; основание системы счисления $b$.

*Выход. Произведение $w = uv = w_1 w_2 \ldots w_{m+n}$.

1. Присвоить $t = 0$.
2. Для $s$ от $0$ до $m + n - 1$ с шагом 1 выполнить шаги 3 и 4.
3. Для $i$ от $0$ до $s$ с шагом 1 выполнить присвоение $t~=~t~+~u_{n - i}~\cdot~v_{m - s + i}$.
4. Присвоить $w_{m + n - s} = t \pmod{b}, t = \left[ \frac{t}{b} \right]$. Результат: $w$.

## Деление многоразрядных целых чисел

*Вход. Числа $u = u_n \ldots u_1 u_0$, $v = v_t \ldots v_1 v_0, n \ge t \ge 1, v_t \ne 0$.

*Выход. Частное $q = q_{n-t} \ldots q_0$, остаток $r = r_t \ldots r_0$.

1. Для $j$ от $0$ до $n - t$ присвоить $q_j = 0$.
2. Пока $u \ge v b^{n - t}$, выполнять: $q_{n - t} = q_{n - t} + 1, u = u - v b^{n - t}$.
3. Для $i = n, n - 1, \ldots, t + 1$ выполнять пункты 3.1 -- 3.4:
	3.1. если $u_i \ge v_t$, то присвоить $q_{i - t - 1} = b - 1$, иначе присвоить $q_{i - t - 1} = \frac{u_i b + u_{i - 1}}{v_t}$.
	3.2. пока $q_{i - t - 1} (v_t b + v_{t - 1}) > u_i b^2 + u_{i - 1} b + u_{i - 2}$ выполнять $q_{i - t - 1} = q_{i - t - 1} - 1$.
	3.3. присвоить $u = u - q_{i - t - 1} b^{i - t - 1} v$.
	3.4. если $u < 0$, то присвоить $u = u + v b^{i - t - 1}$, $q_{i - t - 1}~=~q_{i - t - 1}~-~1$.
4. $r = u$. Результат: $q$ и $r$.

# Выполнение лабораторной работы

1. Написал блок данных (рис. -@fig:001)

![Начальные данные](image/1.png){ #fig:001 width=70% }

2. Написал алгоритм сложения неотрицательных целых чисел  (рис. -@fig:002)

![Алгоритм Сложение неотрицательных целых чисел](image/2.png){ #fig:002 width=70% }


3. Написал алгоритм вычитания неотрицательных целых чисел (рис. -@fig:003)

![Алгоритм вычитания неотрицательных целых чисел](image/3.png){ #fig:003 width=70% }

4. Написал алгоритм умножения неотрицательных целых чисел столбиком(рис. -@fig:004)(рис. -@fig:005)

![Алгоритм умножения неотрицательных целых чисел столбиком первая часть](image/4.png){ #fig:004 width=70% }

![Алгоритм умножения неотрицательных целых чисел столбиком вторая часть](image/5.png){ #fig:005 width=70% }

5. Написал алгоритм быстрого столбика (рис. -@fig:006)

![Алгоритм быстрого столбика](image/6.png){ #fig:006 width=70% }

6. Написал алгоритм деления многоразрядных целых чисел (рис. -@fig:007)(рис. -@fig:008)

![Алгоритм деления многоразрядных целых чисел](image/7.png){ #fig:007 width=70% }


![Алгоритм деления многоразрядных целых чисел](image/8.png){ #fig:008 width=70% }

7. Получил результат (рис. -@fig:009)

![Результат алгоритмов](image/9.png){ #fig:009 width=70% }

# Выводы

Изучал задачу представления больших чисел, познакомились с вычислительными алгоритмами и реализовали их.

# Список литературы


1. [Длинная арифметика от Microsoft](https://habr.com/ru/post/207754/)
2. [Как оперировать числами, не помещающимися ни в один из числовых типов](https://programforyou.ru/poleznoe/dlinnaya-arifmetika-kak-operirovat-chislami-ne-pomeshchayushchimisya-ni-v-odin-iz-chislovyh-tipov)
