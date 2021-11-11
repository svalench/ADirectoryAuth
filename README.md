# Сервис проверки никнейма и пароля пользователя в Active Directory  

## Переменные

Для работы проекта необходимо определить 2 константы в файле .env  
LDAP_SERVER_HOST - хост сервера с AD  
LDAP_SERVER_PORT - порт сервера с AD  

Для примера есть файл .env.example. Переименуйте его в .env 
и определите там переменные.

## Развертывание без Докера

> ```python3 -m venv env``` (Linux) ```py -m venv env``` Window   
> ```source env/bin/activate``` активировать окружение в Linux, ```.\env\Scripts\activate``` в Window  
> ```pip install -r requirements.txt``` Установка зависимостей  
> ```uvicorn main:app --reload``` - запуск проекта