# Converter

## Задание

Флаг находится в /flag.txt.

Ссылка на сервис: <http://converter.2018.cyberchallenge.ru>

## Решение

Переходим по ссылке видим кнопку загрузки, нам необходимо загрузить скрипт, который бы вывел флаг на экран(команда **passthru("cat /flag.txt");** для PHP).

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Converter/Converter_1.png"
     width="70%"></img>

Загружаем на сайт code.php, по логике необходимо было догадаться, что он перед тем как создает .png файл, в той же папке сохраняет оригинальный файл,
в HTML коде берем ссылку на полученное изображение и вместо ссылки на изображение что-то типа **/5ba0e747e204b.png** вставляем **/code.php**
и при переходе на него видим флаг: **CC{n0w_g0_4nd_f1nd_s0m3_r3al_vu1n5_1n_r3al_softw4r3}**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/ImageBox/Converter_2.png"
     width="70%"></img>
