# Intercepted

## Задание

Мы перехватили какой-то странный интернет-трафик. Нам кажется, эти люди что-то замышляют. Впрочем, люди ли?

## Решение

Прикрепленный файл **intercepted.pcap** можно открыть в программе **WireShark**, смотрим протокол FTP

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Forensic/Intercepted/IC_1.png"
     width="70%"></img>
	 
В этом протоколе видно IP адрес - **159.169.59.245**, логин - **anunak** и пароль - **subdue_the_humanity**

Переходим по ссылке <ftp://159.69.59.245> логинимся и видим файл **flag.txt** , в котором и лежит флаг: **CC{1_s33_wh47_y0u_d1d_7h3r3}**

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Forensic/Intercepted/IC_2.png"
     width="70%"></img>
