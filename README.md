 🎁 Freebie Tracker

A simple SQLAlchemy-based Python application for tracking developer freebies ("swag") from various tech companies. Built as a Phase 3 code challenge to practice object-oriented design, database relationships, and CRUD operations using SQLAlchemy and Alembic.

 📦 Features
- Track **companies**, **developers**, and the **freebies** they exchange
- Many-to-many relationship between Developers and Companies via Freebies
- ORM-based queries using SQLAlchemy
- Migration handling via Alembic
- Interactive testing via ipdb console
- Custom methods for querying and manipulating data

 🛠 Technologies
- Python 3
- SQLAlchemy (ORM)
- Alembic (for database migrations)
- SQLite (for local development)
- Pipenv (virtual environment and dependency management)
- ipdb (interactive debugging)

 📁 Project Structure
freebie-tracker/
├── models.py # SQLAlchemy models
├── seed.py # Script to populate initial database data
├── debug.py # Console for testing models
├── freebies.db # SQLite database (auto-generated)
├── migrations/ # Alembic migration files
├── Pipfile # Pipenv dependencies
├── alembic.ini # Alembic config
└── README.md # Project documentation
