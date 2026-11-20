# Task Manager

A web application developed with **Python and Django** for managing and organizing daily tasks. The application allows users to create activities, set priorities, track progress, and manage their tasks through a simple and intuitive interface.

This project was developed as a learning experience to practice web development, database integration, and CRUD operations using Django.

## Features

- **Task management:** create, edit, and delete tasks.
- **Status control:** mark tasks as completed or reopen them.
- **Priority levels:** classify tasks as low, medium, or high priority, with visual indicators.
- **Task filtering:** display all tasks, pending tasks, or completed tasks.
- **Dashboard summary:** view the total number of tasks, pending tasks, and completed tasks.
- **Administration panel:** Django admin interface available at `/admin/`.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django 4.2 | Web framework |
| SQLite | Database |
| HTML5 | Page structure |
| CSS3 | Styling and user interface |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vittimel/task-manager.git
cd task-manager
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply database migrations

```bash
python manage.py migrate
```

### 4. Start the development server

```bash
python manage.py runserver
```

### 5. Access the application

Open your browser and navigate to:

`http://127.0.0.1:8000/`

### Admin Panel

To access the Django administration panel, create a superuser:

```bash
python manage.py createsuperuser
```

Then navigate to:

`http://127.0.0.1:8000/admin/`

## Learning Objectives

This project provided practical experience with:

- Web application development using Django.
- Database modeling and data manipulation.
- CRUD operations.
- Django models, views, URLs, and templates.
- Backend and frontend integration.
- Python project organization and structure.

## Author

**Melissa Forti Vitti**

Computer Engineering Student

[GitHub](https://github.com/vittimel)
