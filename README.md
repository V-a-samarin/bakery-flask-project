# Bakery Flask Project

Веб-приложение для автоматизации деятельности пекарни и кондитерской.

Проект соответствует описанию практической работы: Python + Flask + SQLite + Jinja2, административная панель, авторизация, управление продукцией и клиентами, заказы и отчётность. В исходном отчёте также указана ссылка на GitHub-репозиторий проекта. fileciteturn0file0L28-L31

## Возможности

- регистрация и авторизация пользователей;
- административная панель со статистикой;
- управление товарами;
- управление клиентами;
- оформление заказов;
- автоматическое уменьшение остатка товара;
- отчёт по продажам с фильтрацией;
- SQLite через Flask-SQLAlchemy;
- адаптивный интерфейс Bootstrap 5.

## Структура

```text
bakery-flask-project/
├── app.py
├── run.py
├── requirements.txt
├── README.md
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth.py
│   ├── dashboard.py
│   ├── products.py
│   ├── clients.py
│   ├── orders.py
│   ├── reports.py
│   ├── templates/
│   └── static/
└── instance/
    └── bakery.db  # создаётся автоматически при запуске
```

## Запуск

### Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

После запуска откройте:

`http://127.0.0.1:5000`

## Данные для первого входа

- Логин: `admin`
- Пароль: `admin123`

После входа пароль можно заменить, а `SECRET_KEY` рекомендуется изменить в `app/__init__.py`.

## GitHub

```bash
git init
git add .
git commit -m "Initial bakery Flask project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bakery-flask-project.git
git push -u origin main
```

В отчёте пользователя указан репозиторий `vasamarin/bakery-flask-project`; при загрузке этого архива можно использовать новый репозиторий или заменить содержимое существующего. fileciteturn0file0L81-L85
