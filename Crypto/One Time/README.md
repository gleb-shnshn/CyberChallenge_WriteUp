# One Time

## Задание

Я нашел код своего друга. Похоже на криптографию, но чего-то точно не хватает. Он очень скромный, и все, что я о нем знаю — это то, что он помешан на песне «Rick Astley — Never gonna give you up». Но ты ведь мне поможешь?

## Решение

Название говорит о том, что шифрование - One Time Pad, тогда у нас есть специальный сайт <https://toolbox.lotusfa.com/crib_drag/>.

<img src="https://raw.githubusercontent.com/gleb270/CyberChallenge_WriteUp/master/Crypto/One Time/OT.png"
     width="70%"></img>

В поле **Ciphertext1** и **Ciphertext2** вставляем значения из прикрепленного файла **crypto.py** , пробуем подбирать **Crib words** так, чтобы в первой строчке были строчки из песни **Rick Astley — Never gonna give you up** 
Постепенно подбираем строку и получаем в **Crib words**

the flag for this task is cc curly bracket zero n three underscore seven one m three underscore p four d underscore one five underscore five three cur three underscore zero nly underscore zero nc three curly bracket.

Ее можно собрать в флаг: **CC{0n3_71m3_p4d_15_53cur3_0nly_0nc3}**
