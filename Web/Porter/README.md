# No Comments

## Задание

Веб-сервис расположен на каком-то из портов в диапазоне 1000-2000 на сервере 2018.cyberchallenge.ru. Сможешь ли ты найти его?

## Решение

Используем утилиту nmap для Linux для нахождения свободных портов **nmap -p 1000-2000 2018.cyberchallenge.ru, которая говорит нам о том что свободный порт 1337. 
Переходим по ссылке в браузере <2018.cyberchallenge.ru:1337>, тыкаем на ссылку, она перенаправляет сначала на flag.html, а потом обратно.

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Porter/FlagIsHere.png"
     width="70%"></img>

Тогда смотрим код страницы по ссылке <view-source:http://2018.cyberchallenge.ru:1337/flag.html> видим флаг: **CC{ra8Zb53uJeA_this_was_a_trick}**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Porter/Source.png"
     width="70%"></img>
