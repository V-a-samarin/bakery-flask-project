# Архитектура проекта

## Логическая схема

Пользователь → Flask Web Server → Blueprints (Auth / Dashboard / Products / Clients / Orders / Reports) → SQLAlchemy ORM → SQLite.

## Слои

1. Presentation: Jinja2 templates + Bootstrap 5 + CSS.
2. Web/Application: Flask Blueprints и маршруты.
3. Business logic: обработка авторизации, товаров, клиентов, заказов и отчётности.
4. Data access: Flask-SQLAlchemy.
5. Storage: SQLite.

## Основные сущности

User, Product, Client, Order.

## Поток заказа

Форма заказа → проверка товара и остатка → расчёт суммы → создание Order → уменьшение Product.stock → сохранение в SQLite → вывод в разделе заказов и отчётности.
