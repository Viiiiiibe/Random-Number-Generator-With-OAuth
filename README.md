# random-number-generator
### Генератор случайных чисел с OAuth

Сервер каждые пять секунд генерирует случайные данные (число).

При открытии страница предлагает авторизоваться, есть возможность сделать oauth авторизацию github. На странице, которую видит пользователь после прохождения авторизации, показывается актуальное генерируемое сервером число без обновления страницы пользователем (через WebSocket) и ссылка для выхода из аккаунта. Неавторизованные пользователи число не видят. Сгенерированные данные для всех пользователей совпадают.

## Локальный запуск проекта
- Создать приложения на GitHub (если его нет)

1) Перейти на [GitHub Developer Settings](https://github.com/settings/developers)

2) Нажать "New OAuth App" и заполнить форму: 
Application name: Название нового приложения.
Homepage URL: URL сайта (например, http://localhost:8000/ для локальной разработки).
Authorization callback URL: http://localhost:8000/accounts/github/login/callback/.
3) Сохранить изменения. Получить Client ID и Client Secret.
- Рядом с файлом .env.example разместить .env файл. Env переменные:
```
SECRET_KEY='1234567890'
client_id='Ваш Client ID'
secret='Ваш Client Secret'
```
- В основной папке установить и активировать виртуальное окружение
```console  
python -m venv venv
```
```console  
.\venv\Scripts\activate.bat
```

- Установить используемые библиотеки из файла requirements.txt
```console  
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполнить команду для миграций:
```console  
python manage.py migrate
```
- В папке с файлом manage.py выполнить команду для запуска локального сервера:
```console  
python manage.py runserver
```
Сайт отобразится по адресу http://127.0.0.1:8000/
