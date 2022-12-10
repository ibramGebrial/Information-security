---
## Front matter
lang: ru-RU
title: Дискретное логарифмирование в конечном поле
author: |
	Гебриал Ибрам Есам Зекри \inst{1}
	
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
	
date: 2022 Moscow, Russia

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Цель работы

## Цель работы

Реализация алгоритма, реализующий p-метод Полларда для задач дискретного логарифмирования.

# Задачи

## Задачи

1. Реализовать алгоритм, реализующий p-метод Полларда для задач дискретного логарифмирования.



# Реализация

##

1. Написал функцию ext_euclid и inverse (рис. -@fig:001)

![Функция для расширенного алгоритма Евклида и обратного значнения](image/1.png){ #fig:001 width=70% }

##

2. Написал функцию xab  (рис. -@fig:002)

![Функция xab](image/2.png){ #fig:002 width=70% }

##

3. Написал функцию pollard (рис. -@fig:003)

![Функция для алгоритма pollard](image/3.png){ #fig:003 width=70% }

##

4. Написал функцию verify и блок работы программы(рис. -@fig:004)

![Функция verify и блок работы программы](image/4.png){ #fig:004 width=70% }


## Результат

![Результат алгоритма](image/5.png){ #fig:005 width=70% }


## Вывод


Реализовал реализующий p-метод Полларда для задач дискретного логарифмирования.

## {.standout}

Спасибо за внимание 
