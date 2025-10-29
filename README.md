
# CRUD Application (Django + PostgreSQL)

This is a simple CRUD (Create, Read, Update, Delete) application built using:
- **Django (Backend Framework)**
- **PostgreSQL (Database)**
- **Django REST Framework (API Layer)**

The project exposes RESTful endpoints for managing contact records.

---

## Features
- Create new contacts
- Retrieve list of contacts
- Get a single contact by ID
- Update contact details
- Delete a contact

---

## Tech Stack
| Component | Technology |
|----------|------------|
| Backend  | Django + Django REST Framework |
| Database | PostgreSQL |
| Deployment (Optional) | Render |

---

## Project Setup

### 1. Clone the Repository
```sh
git clone <repository-url>
cd <project-folder>
````

### 2. Create Virtual Environment & Install Dependencies

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create `.env` in project root:

```
DATABASE_URL=postgres://YOUR_USER:YOUR_PASSWORD@YOUR_HOST:5432/YOUR_DB_NAME
```

### 4. Apply Migrations

```sh
python manage.py migrate
```

### 5. Run Server

```sh
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| GET    | `/api/contacts/`      | Get all contacts     |
| POST   | `/api/contacts/`      | Create a new contact |
| GET    | `/api/contacts/<id>/` | Get a single contact |
| PUT    | `/api/contacts/<id>/` | Update contact       |
| DELETE | `/api/contacts/<id>/` | Delete contact       |

---

## Deployment on Render (Optional)

1. Create a **Web Service** on Render.
2. Set **Runtime** to: `Python`
3. Add your GitHub repository.
4. Add your `DATABASE_URL` in Render → Environment Variables.
5. Add **Procfile** to project root:

```
web: gunicorn <project_name>.wsgi
```

(Replace `<project_name>` with the folder containing settings.py)

Deploy.

---

## Notes

* Ensure PostgreSQL is running before starting the server.
* If using Supabase, simply replace `DATABASE_URL` with Supabase connection string.

---

## License

This project is open-source and free to use for learning and development.

```


Just tell me: **"Make demo ready"** or **"Make architecture diagram"**.
```
