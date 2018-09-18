# Just Add

## Задание

Знание недостатков языка PHP необходимо начинающему специалисту в области информационной безопасности. Продемонстрируйте мне ваши навыки, и вы получите флаг.

Ссылка на сервис: <http://inc.2018.cyberchallenge.ru>

## Решение

Переходим по ссылке видим первую страницу, т.к. в задании говорится прибавляй, меняем GET параметр на 2 и 3. Смотрим что тут ничего интересного нет, но можно использовать уязвимость PHP

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Just Add/JA_123.png"
     width="70%"></img>

Тогда переходим по ссылке <http://inc.2018.cyberchallenge.ru/index.php?page=php://filter/convert.base64-encode/resource=index.php> 
с помощью которой получаем исходный код страницы в base64 по протоколу php, после этого декодируем, например, здесь <https://www.base64decode.org>, и в коде видим, что он запрещает переходить на /th1s_1s_the_h1dd3n_fl4g.7x7

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Just Add/Code.png"
     width="70%"></img>

Вместо этого переходим по ссылке <http://inc.2018.cyberchallenge.ru/index.php?page=/./th1s_1s_the_h1dd3n_fl4g.7x7> и видим флаг: **CC{leaRnIng_phP}**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Just Add/Flag.png"
     width="70%"></img>
