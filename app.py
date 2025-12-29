
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        if not name:
            return render_template("error.html", message="Name is required")
        if not month:
            return render_template("error.html", message="Month is required")
        try:
            month = int(month)
            if month < 1 or month > 12:
                return render_template("error.html", message="Month must be between 1 and 12")
        except ValueError:
            return render_template("error.html", message="Month must be a valid number")
        
        if not day:
            return render_template("error.html", message="Day is required")
        try:
            day = int(day)
            if day < 1 or day > 31:
                return render_template("error.html", message="Day must be between 1 and 31")
        except ValueError:
            return render_template("error.html", message="Day must be a valid number")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * from birthdays")

        return render_template("index.html", birthdays=birthdays)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    """Delete a birthday entry from the database"""
    # Support both GET and POST methods
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    
    if not id:
        return render_template("error.html", message="ID is required")
    
    try:
        id = int(id)
    except ValueError:
        return render_template("error.html", message="Invalid ID format")
    
    # Check if entry exists before deleting
    entry = db.execute("SELECT * FROM birthdays WHERE id = ?", id)
    if not entry:
        return render_template("error.html", message="Entry not found")
    
    db.execute("DELETE FROM birthdays WHERE id = ?", id)
    
    return redirect("/")
