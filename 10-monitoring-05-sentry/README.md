# Домашнее задание к занятию "10.05. Sentry"

## Задание 1.  
Зарегистрировался на [sentry.io](https://sentry.io/), используя GitHub-аккаунт, создал python-проект, вставил предложенный код в своё приложение и тут же получил первый issue :)
![sentry01-2.png](sentry01-2.png)  

Привожу скриншот раздела Projects  
![sentry01-1.png](sentry01-1.png)

## Заданеи 2.

В данном задании возник один вопрос, который, впрочем, не помешал выполнению задания.  
Где именно нужно было сделать ```нажмите Generate sample event```? В интерфейсе я такого не нашёл, в системе помощи тоже о таком функционале упоминаний не нашёл.  

Тем не менее, у меня есть рабочий [python-код](demo.py), который позволяет эти события гененрировать.  
Скриншот со Stack srace  
![sentry02-1.png](sentry02-1.png)  

Скриншот с Resolved Issue  
![sentry02-2.png](sentry02-2.png)  

## Задание 3.  
Оповещение получено на e-mail:  
![sentry03-1.png](sentry03-1.png)

## Задание со *.  
На данном этапе у меня уже создан небольшой [python-код](demo.py), но я решил поэкспериментировать ещё и [golang](demo.go). Хочу сказать, что не зря. В go мне потребовалось чуть больше движений, да и большая часть горутин уже перехватывает исключения, возвращая ошибки. В данном примере я пробовал передавать как отладочную информацию, так и стек трейс из кода ошибки функции http.ListenAndServe при попытке запуска на занятом порту.  

![sentry04-1.png](sentry04-1.png)  

![sentry04-2.png](sentry04-2.png)  