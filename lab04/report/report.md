---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе 4"
subtitle: "Вычисление наибольшего общего делителя"
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

Реализация алгоритмов вычисления наибольшего общего делителя (Евклида).
 
# Теоретические сведения

Алгоритм Евклида — это способ нахождения наибольшего общего делителя (НОД) двух целых чисел. Оригинальная версия алгоритма, когда НОД находится вычитанием, была открыта Евклидом (III в. до н. э). В настоящее время чаще при вычислении НОД алгоритмом Евклида используют деление, так как данный метод эффективнее.

**Вычисление НОД делением**

Наибольший общий делитель пары чисел – это самое большое число, которое нацело делит оба числа пары. Пусть требуется вычислить НОД для чисел 108 и 72. Алгоритм вычисления делением будет таковым:

1. Разделим большее число (делимое) на меньшее (делитель): 108 / 72 = 1, остаток 36.
2. Поскольку остаток не был равен нулю, то сделаем делитель делимым, а остаток – делителем: 72 / 36 = 2, остаток 0.
3. Когда остаток равен нулю, то делитель является искомым НОД для пары заданных чисел. То есть НОД(108, 72) = 36. Действительно, 108 / 36 = 3 и 72 / 36 = 2.[1]

**Расширенный алгоритма Евклида**

Расширенным алгоритм называется не из-за более высокой скорости работы или более сложной реализации, а потому что он позволяет извлекать из входных данных дополнительную информацию.

Расширенный алгоритм также находит наибольший общий делитель, а ещё он определяет два коэффициента x и y, такие что:

ax + by = gcd(a,b), где gcd – это функция по нахождения НОД.

Иными словами, алгоритм находит наибольший делитель и его линейное представление.

gcd – это аббревиатура, которую часто используют для обозначения функции по назначению НОД:

g – Greatest (наибольший);

c – Common (общий);

d – Divisor (делитель).

**Бинарный алгоритм Евклида**

Суть бинарного алгоритма точно такая же — найти наибольший делитель. От классического он отличается только способом реализации.

Вместо классических арифметических операций, в бинарном алгоритме Евклида используются только битовые сдвиги влево и вправо, которые соответствуют умножению и делению на 2.[2]




# Выполнение лабораторной работы

1. Написал функцию evklid_nod для вычисления алгоритма Евклида. (рис. -@fig:001)

Алгоритм нахождения НОД делением:

1. Большее число делим на меньшее.
2. Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).
3. Если есть остаток, то большее число заменяем на остаток от деления.
4. Переходим к пункту 1.

![Функция для вычисления алгоритма Евклида](image/1.png){ #fig:001 width=70% }

2. Написал функцию evklid_binary для вычисления бинарного алгоритма Евклида. (рис. -@fig:002)

	1. Сначала положим g= 1 

	2. Пока оба числа a и b четные, выполнить $a= \frac{a}{2}$, $b= \frac{b}{2}$, g= 2g до получения хотя одного нечетного значения a или b.

	3. Положим u=a, v=b

	4. Пока u \neq 0:
		
		1. Пока u четное, полагать $u= \frac{u}{2}$
		2. Пока v четное, полагать $v= \frac{v}{2}$
		3. При u \geq v  положим u= u-v. В противном случае положим v=v-u 
	5. Положим d=gv
	6. Получим результат d

![Функция для вычисления бинарного алгоритма Евклида](image/2.png){ #fig:002 width=70% }

3. Написал функцию evklid_extend для вычисления расширенного алгоритма Евклида. (рис. -@fig:003)

Сначала проверяется, равно ли первое число нулю, если это так, то второе число является делителем, а коэффициенты равны 0 и 1, так как «num1 * x + num2 * y = y» в том случае, если y = 1, а левое произведение равно нулю.

Функция возвращает три числа: делитель, коэффициент x и коэффициент y.

![Функция для вычисления вычисления расширенного алгоритма Евклида.](image/3.png){ #fig:003 width=70% }

4. Написал функцию evklid_binary_extend для вычисления расширенного бинарного алгоритма Евклида. (рис. -@fig:004) (рис. -@fig:005)


	1. Сначала положим g= 1 

	2. Пока оба числа a и b четные, выполнить $a= \frac{a}{2}$, $b= \frac{b}{2}$, g= 2g до получения хотя одного нечетного значения a или b.

	3. Положим u=a, v=b, A=1, B= 0, C= 0, D=1.

	4. Пока u \neq 0:
		
		1. Пока u четное, полагать $u= \frac{u}{2}$
		2. Если оба числа A и B четные, полагать $A= \frac{A}{2}$, $B= \frac{B}{2}$. В противном случае положить $A= \frac{A+b}{2}$, $B= \frac{B-a}{2}$
		3. Пока v четное, полагать $v= \frac{v}{2}$
		4. Если оба числа C и D четные, полагать $C= \frac{C}{2}$, $D= \frac{D}{2}$. В противном случае положить $C= \frac{C+b}{2}$, $D= \frac{D-2}{2}$	
		5. При u \geq v  положим u= u-v, A= A-C, B = B-D. В противном случае положим v=v-u, C= C-A, D= D-B. 
	5. Положим d=gv, x= C, y=D
	6. Получим результат d,x,y

![Функция для вычисления расширенного бинарного алгоритма Евклида. Первая часть](image/4.png){ #fig:004 width=70% }

![Функция для вычисления расширенного бинарного алгоритма Евклида. Вторая часть](image/5.png){ #fig:005 width=70% }

5. Получил результат (рис. -@fig:006)

![Результат алгоритмов](image/6.png){ #fig:006 width=70% }

# Выводы

Реализовал алгоритм вычисления наибольшего общего делителя (Евклида).

# Список литературы

1. Алгоритм Евклида [Электронный ресурс] - Режим доступа: https://scienceland.info/

algebra8/euclid-algorithm

2. Бинарный алгоритм вычисления НОД [Электронный ресурс] - Режим доступа: https://intellect.icu/binarnyj-algoritm-vychisleniya-nod-4394