# Octocat

## Задание

Unnamed repository; edit this file 'description' to name the repository.

Ссылка на сервис: <http://octocat.2018.cyberchallenge.ru>

## Решение

Название и описание наталкивают на мысль, о том, что задание связано с git.

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Octocat/Sign.png"
     width="40%"></img>

Качаем GitTools, качаем Dump сайта командой **./gitdumper.sh http://octocat.cyberchallenge.ru/.git/ Dump**
разархивируем Dump с помощью **./extractor.sh ~/Desktop/GitTools/Dumper/Dump Dump**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Octocat/Dump.png"
     width="70%"></img>

В папке Dump находим 2 commit-a в одном из которых в файле flag.php есть флаг: **CC{CseK6Eo762c_octocat_is_fuuuuuuuun}**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/Octocat/Flag.png"
     width="70%"></img>
