[Read in English](README.md)
---

# ✒️ Flask Blog Platform

Полнофункциональное веб-приложение для ведения блога, созданное на Flask. Проект сочетает в себе классический серверный рендеринг (SSR) с помощью Jinja2 и современный динамический интерфейс для лайков и комментариев, работающий через REST API.

---

## 🚀 О проекте

Этот проект демонстрирует классический подход к веб-разработке с использованием фреймворка Flask. Архитектура проекта разделена на логические модули с помощью **Blueprints**, что обеспечивает чистоту и масштабируемость кода.

*   **Бэкенд (Flask):** Реализует всю основную логику: аутентификацию пользователей, управление сессиями, CRUD-операции для статей и предоставление API для интерактивных элементов.
*   **Фронтенд (Jinja2 & Vanilla JS):** Основная часть интерфейса рендерится на сервере с помощью шаблонизатора Jinja2. Динамические элементы, такие как лайки и комментарии, работают асинхронно через JavaScript (fetch API) без перезагрузки страницы.

---

## 🛠️ Стек технологий

*   **Бэкенд:**
    *   ![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
    *   ![Flask](https://img.shields.io/badge/Flask-2.2.2-000000?style=for-the-badge&logo=flask)
    *   ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-DB4437?style=for-the-badge&logo=sqlalchemy)
    *   ![Jinja2](https://img.shields.io/badge/Jinja2-template_engine-B42B2B?style=for-the-badge)
*   **Фронтенд:**
    *   ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
    *   ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
    *   ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript)
*   **База данных и Миграции:**
    *   ![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite)
    *   ![Alembic](https://img.shields.io/badge/Alembic-migrations-4E2A84?style=for-the-badge)
*   **Инструменты и Библиотеки:**
    *   `Flask-Login` (Управление сессиями)
    *   `Flask-WTF` & `WTForms` (Формы и CSRF-защита)
    *   `Werkzeug` (Хэширование паролей)
    *   `Flask-Migrate` (Интеграция Alembic)
    *   `python-dotenv` (Переменные окружения)

---

## ✨ Ключевые возможности

*   **🔐 Аутентификация и Управление пользователями:**
    *   Полный цикл: регистрация, логин, выход из системы.
    *   Управление сессиями с помощью `Flask-Login`.
    *   Безопасное хэширование паролей.
    *   Профиль пользователя с отображением его постов.
    *   Защита форм от CSRF-атак.
*   **📝 Управление контентом:**
    *   Создание статей через защищенные роуты.
    *   Просмотр всех статей на главной странице.
    *   Детальный просмотр каждой статьи на отдельной странице.
    *   Модульная структура кода с использованием `Blueprints` для разделения логики.
*   **🚀 Динамический интерфейс:**
    *   Система лайков "в реальном времени" (без перезагрузки страницы), работающая через API.
    *   Асинхронное добавление и отображение комментариев на странице поста.
*   **📦 Управление базой данных:**
    *   Настроенный механизм миграций с помощью `Flask-Migrate` и `Alembic` для безопасного изменения схемы БД.

---

## 🏁 Начало работы

### Требования
*   Python 3.10+
*   Менеджер пакетов `pip`

### Запуск проекта

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/Varenik-vkusny/Blog.git
    cd Blog
    ```
2.  **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```
3.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Настройте переменные окружения:**
    *   Создайте файл `.env` в корне проекта.
    *   Добавьте в него секретный ключ для работы веб-форм и сессий:
        ```dotenv
        SECRET_KEY='your_super_mega_long_key_that_no_one_knows'
        ```
5.  **Примените миграции базы данных:**
    *   Эта команда создаст файл базы данных `blog.db` с последней версией всех таблиц:
        ```bash
        flask db upgrade
        ```
6.  **Запустите приложение:**
    ```bash
    flask run
    ```
7.  **Готово!** Приложение будет доступно в вашем браузере по адресу: `http://127.0.0.1:5000`.
