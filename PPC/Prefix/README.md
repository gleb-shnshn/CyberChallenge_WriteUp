# Prefix

## Задание

Подберите верный флаг.

Для подключения к сервису воспользуйтесь утилитой netcat следующим образом:
nc prefix.2018.cyberchallenge.ru 9001

## Решение

Сервис отвечает Yes, если присланная строка является началом флага, зная это можно подобрать флаг с помощью **prefix.py**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/PPC/Prefix/Prefix.png"
     width="70%"></img>

В итоге получаем флаг: **CC{too_s1mpl3_t0_brut3}**

