# ImageBox 2

## Задание

Разработчики стартапа ImageBox осознали свою ошибку и пересмотрели свой подход к обеспечению безопасности сервиса. По их словам, теперь хостинг неуязвим. Проверим?

Ссылка на сервис: <http://imageboxhard.2018.cyberchallenge.ru>

## Решение

В отличии от первого ImageBox здесь проверяется, чтобы в файле не было **exec** , **passthru** , **system** , тогда мы используем **echo file_get_contents("/var/flag.txt");** вместо этого

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/ImageBox 2/IB_1.png"
     width="70%"></img>

Если попытаться загрузить **code.php.jpg** он не работает, тогла путем проверок понимаем, что файл убирает htaccess из названия и делаем название файла **code.phtaccesshp.jpg**
Запускаем BurpSuite, отправляем файл, изменяем в пакете имя на **code.php** , заходим на ссылку из HTML кода и получаем флаг: **СС{place for flag}**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/ImageBox 2/IB_2.png"
     width="70%"></img>
