# Birthdays - Web Application

## Description

A simple web application for managing birthdays, created for educational purposes. The application allows users to add birthdays to a database and display a list of all saved entries.

**⚠️ Note: This project is created exclusively for educational purposes and is intended for learning the basics of web development using Flask and SQLite.**

## Technologies

- **Backend**: Python 3, Flask
- **Database**: SQLite (via CS50 SQL library)
- **Frontend**: HTML, CSS, Jinja2 templates
- **Libraries**:
  - Flask - web framework
  - CS50 SQL - simplified library for working with SQLite (used in CS50 educational projects)

## Features

- ✅ Add birthday (name, month, day)
- ✅ Input data validation
- ✅ Display list of all birthdays in a table
- ✅ Error handling with user-friendly messages

## Project Structure

```
birthdays/
├── app.py                 # Main Flask application file
├── birthdays.db           # SQLite database
├── templates/
│   ├── index.html        # Main page with form and table
│   └── error.html        # Error display page
├── static/
│   └── styles.css        # Application styles
└── README.md             # This file
```

## Installation and Setup

### Requirements

- Python 3.x
- Flask
- CS50 SQL library

### Installation Steps

1. Clone the repository or download the project
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install flask cs50
   ```

5. Create the database (if not already created):
   ```bash
   sqlite3 birthdays.db
   ```
   Then execute the SQL command to create the table:
   ```sql
   CREATE TABLE IF NOT EXISTS birthdays (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       month INTEGER NOT NULL,
       day INTEGER NOT NULL
   );
   ```

6. Run the application:
   ```bash
   flask run
   ```

7. Open your browser and navigate to: `http://127.0.0.1:5000`

## Usage

1. On the main page, fill out the form:
   - **Name**: Person's name
   - **Month**: Month (1-12)
   - **Day**: Day (1-31)

2. Click the "Add Birthday" button

3. The new birthday will appear in the "All Birthdays" table

## Implementation Details

- Use of parameterized SQL queries to protect against SQL injection
- Server-side data validation
- Automatic template reloading during development
- Cache disabling for proper development mode operation

## Notes

- The project uses the CS50 SQL library, which is a simplified wrapper for educational purposes
- In production environments, it is recommended to use more advanced ORMs (e.g., SQLAlchemy)
- The SQLite database is stored locally in the `birthdays.db` file

## License

This project is created for educational purposes and is not intended for commercial use.

## Author

Created as part of learning web development.

