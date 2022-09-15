---
## Front matter
lang: ru-RU
title: Шифры простой замены
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

## цель работы

Приобретение навыков программной реализации простых шифров подстановки и замены.

# Задание

## Задание

1. Реализовать шифр Цезарья с произвольным ключом k.

2. Реализовать шифр Атбаш.


# Реализация

## Реализация шифра Цезаря 

Функция caesar для шифрования и расшифровки текста. (рис. -@fig:001)

![Функция для кодирования текста шифром Цезаря ](image/1.png){ #fig:001 width=70% }

##  Реализация шифра Атбаша

Функция atbash для шифрования и расшифровки текста. (рис. -@fig:002)

![Функция для кодирования текста шифром Атбаша](image/2.png){ #fig:002 width=70% }

##  Процесс выполнения

Описан блок выбора нужного метода и ввода текста. (рис. -@fig:003)

![Код для выбора метод шифрования и ввода текста](image/3.png){ #fig:003 width=60% }

# Результат

## Результат

![Получение шифрования и расшифровки текста методом Цезаря ](image/4.png){ #fig:004 width=70% }

## Результат

![Получение шифрования текста методом Атбаша](image/5.png){ #fig:005 width=70% }

## Вывод

Приобрел навыки программной реализации простых шифров подстановки и замены.


## {.standout}

Спасибо за внимание 
