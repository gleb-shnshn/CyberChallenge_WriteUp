# ImageBox

## Задание

Стартап ImageBox объявил о запуске нового облачного сервиса для загрузки и хранения изображений. А чтобы загружать было не так скучно, разработчики еще и спрятали флаг на своем сервере. Попробуйте извлечь его.

Ссылка на сервис: <http://imagebox.2018.cyberchallenge.ru>

## Решение

Переходим по ссылке видим кнопку загрузки, нам необходимо загрузить скрипт, который бы вывел флаг на экран(команда **passthru("cat /etc/flag.txt");** для PHP). При попытке загрузить code.php, выдает ошибку.

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/ImageBox/IB_1.png"
     width="70%"></img>

Тогда с приписываем .jpg и получаем файл code.jpg.php, загружаем на сайт, в HTML коде берем на него ссылку и при переходе на нее видим флаг: **CC{upl0ad_wis3ly}**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Web/ImageBox/IB_2.png"
     width="70%"></img>
