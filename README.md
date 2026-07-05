# Understanding Pydantic with FastAPI

This project is part of my **"Understanding Series"**, where I learn one backend concept at a time by building small, focused projects instead of jumping directly into large applications.

The goal of this project is to understand **Pydantic** from the ground up and learn how it works with **FastAPI** to validate incoming request data.

---

## 📌 Project Objective

To understand:

* What Pydantic is
* Why Pydantic is used in FastAPI
* How `BaseModel` works
* Request body validation
* Automatic data type conversion
* Request validation errors
* FastAPI automatic API documentation (`/docs`)

---

## 🛠️ Technologies Used

* Python 3
* FastAPI
* Pydantic
* Uvicorn

---

## 📂 Project Structure

```
understanding-pydantic/
│
├── main.py
├── .gitignore
└── README.md
```

---

## 🚀 Features

* Create a Student model using `BaseModel`
* Validate incoming request data
* Automatically reject invalid requests
* Automatically convert compatible data types
* Generate interactive API documentation using Swagger UI

---

## 📖 Concepts Learned

* Creating Pydantic models
* Data validation
* Type annotations
* Automatic type conversion
* JSON request bodies
* FastAPI request handling
* API testing using Swagger UI

---

## ▶️ How to Run

### Install dependencies

```bash
pip install fastapi uvicorn
```

### Start the server

```bash
uvicorn main:app --reload
```

### Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📌 Sample Request

```json
{
    "name": "Rahul",
    "age": 21
}
```

---

## 📌 Sample Response

```json
{
    "message": "Student Created",
    "student": {
        "name": "Rahul",
        "age": 21
    }
}
```

---

## 💡 Key Learning

One of the most important things I learned is that **Pydantic validates data before it reaches the FastAPI endpoint**. If the incoming data does not match the expected schema, FastAPI automatically returns a validation error and the endpoint function is not executed.

I also learned that Pydantic performs **type coercion** by default. For example, a value like `"21"` can be converted into the integer `21` when appropriate, while invalid values such as `"Twenty"` are rejected.

---

## 🎯 Future Improvements

* Add optional fields
* Add custom validators
* Use `StrictInt` and `StrictStr`
* Implement nested Pydantic models
* Integrate with a SQLite database
* Build a complete CRUD API using FastAPI and Pydantic

---

## 📚 Learning Series

This repository is part of my backend and AI engineering learning journey, where each repository focuses on understanding one concept thoroughly before combining them into larger real-world projects.

Planned repositories include:

* Understanding FastAPI
* Understanding SQLite
* Understanding PostgreSQL
* Understanding MongoDB
* Understanding REST APIs
* Understanding Authentication (JWT)
* Understanding Docker
* Understanding LangChain
* Understanding RAG
* Understanding MCP
* Understanding LangGraph

---

**Author:** Choudavarapu Naga Varun

Learning by building one concept at a time.
