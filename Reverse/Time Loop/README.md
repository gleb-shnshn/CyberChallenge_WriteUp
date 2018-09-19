# Time Loop

## Задание

Если вы сможете остановить время, то я отдам вам флаг.

Обратите внимание, что данный исполняемый файл предназначен для запуска под операционной системой семейства GNU/Linux.

## Решение

Прикрепленный файл **timeloop** надо открыть в IDA Pro и Hex-Rays.
	 
<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Reverse/Time Loop/TL_1.png"
     width="70%"></img> 
	 
Функция **time(0)** которая выдает **unix-time** проверяет равенство времени 123456, тогда мы идем в конвертер <http://i-leon.ru/tools/time> коневертируем время в обычный вид.

Получаем **02 Jan 1970 10:17:36** , редактируем так чтобы в нашем часовом поясе показывало именно **123456**, например с помощью **ltrace**

У меня получилось **02 Jan 1970 5:17:36**

Запускаем консоль в **Linux** и вписываем туда **for ((i=1; i<=10000 ; i++)); do date --set "02 Jan 1970 5:17:36"; done**

Это нужно, чтобы время менялось чаще чем его проверяет **timeloop**

А в другой консоли запускаем **./timeloop** ждем несколько проверок и получаем флаг: **CC{Can_you_really_stop_the_time?}** 
	 
<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Reverse/Time Loop/TL.png"
     width="70%"></img> 