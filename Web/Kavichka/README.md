# Kavichka

## Задание

Необходимо выполнить вход под учетной записью администратора. Обычное такое задание с кавычками. Классика...

Ссылка на сервис: <http://kavichka.2018.cyberchallenge.ru>

## Решение

Название намекает на использование SQL Injection связанное с кавычкой. 

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Kavichka/Kavichka_1.png"
     width="70%"></img>
	 
Используем логин **admin' or "1"=="1";**, а пароль - **password** логинимся и видим флаг: **CC{4crgYRC45NY_is_this_flag}**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Kavichka/Kavichka_2.png"
     width="70%"></img>
