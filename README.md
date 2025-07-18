[Читать на русском](README_RU.md)
---

# ✒️ Flask Blog Platform

A full-featured blog web application built with Flask. This project combines classic Server-Side Rendering (SSR) using Jinja2 with a modern, dynamic interface for likes and comments powered by a REST API.

---

## 🚀 About The Project

This project demonstrates a classic approach to web development using the Flask framework. The application's architecture is organized into logical modules using **Blueprints**, ensuring clean and scalable code.

*   **Backend (Flask):** Implements all core business logic, including user authentication, session management, CRUD operations for articles, and providing an API for interactive elements.
*   **Frontend (Jinja2 & Vanilla JS):** The main interface is rendered on the server side with the Jinja2 templating engine. Dynamic features like likes and comments are handled asynchronously using JavaScript (Fetch API) without page reloads.

---

## 🛠️ Tech Stack

*   **Backend:**
    *   ![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
    *   ![Flask](https://img.shields.io/badge/Flask-2.2.2-000000?style=for-the-badge&logo=flask)
    *   ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-DB4437?style=for-the-badge&logo=sqlalchemy)
    *   ![Jinja2](https://img.shields.io/badge/Jinja2-template_engine-B42B2B?style=for-the-badge)
*   **Frontend:**
    *   ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
    *   ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
    *   ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript)
*   **Database & Migrations:**
    *   ![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite)
    *   ![Alembic](https://img.shields.io/badge/Alembic-migrations-4E2A84?style=for-the-badge)
*   **Tools & Libraries:**
    *   `Flask-Login` (Session Management)
    *   `Flask-WTF` & `WTForms` (Forms and CSRF Protection)
    *   `Werkzeug` (Password Hashing)
    *   `Flask-Migrate` (Alembic Integration)
    *   `python-dotenv` (Environment Variables)

---

## ✨ Key Features

*   **🔐 Authentication & User Management:**
    *   Full user lifecycle: registration, login, logout.
    *   Session management powered by `Flask-Login`.
    *   Secure password hashing.
    *   User profile page displaying the user's own posts.
    *   Protection against CSRF attacks on all forms.
*   **📝 Content Management:**
    *   Create articles via protected routes.
    *   View all articles on the main page.
    *   View a detailed page for each article.
    *   Modular code structure using `Blueprints` to separate concerns.
*   **🚀 Dynamic Interface:**
    *   Real-time like system (no page reload) powered by a REST API.
    *   Asynchronous adding and displaying of comments on the article detail page.
*   **📦 Database Management:**
    *   A robust database migration system using `Flask-Migrate` and `Alembic` for safe schema evolution.

---

## 🏁 Getting Started

### Prerequisites
*   Python 3.10+
*   `pip` package manager

### Installation & Launch

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Varenik-vkusny/Blog.git
    cd Blog
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    *   Create a `.env` file in the project's root directory.
    *   Add a secret key for web forms and sessions:
        ```dotenv
        SECRET_KEY='your_super_mega_long_key_that_no_one_knows'
        ```
5.  **Apply database migrations:**
    *   This command will create the `blog.db` database file with the latest schema:
        ```bash
        flask db upgrade
        ```
6.  **Run the application:**
    ```bash
    flask run
    ```
7.  **Done!** The application will be available in your browser at `http://127.0.0.1:5000`.
