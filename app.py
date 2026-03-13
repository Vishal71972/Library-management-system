from flask import Flask, render_template, request, redirect
import mysql.connector
import config

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host=config.DB_HOST,

    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

cursor = db.cursor()


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    user_id = request.form["user_id"]
    password = request.form["password"]
    role = request.form["role"]

    if role == "admin":

        cursor.execute(
            "SELECT * FROM admin WHERE admin_id=%s AND password=%s",
            (user_id, password)
        )

        data = cursor.fetchone()

        if data:
            return redirect("/admin_dashboard")


    elif role == "student":

        cursor.execute(
            "SELECT * FROM students WHERE student_id=%s AND password=%s",
            (user_id, password)
        )

        data = cursor.fetchone()

        if data:
            return redirect("/student_dashboard")

    return "Invalid Login"

# admin dashboard route
@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

#student dashboard route
@app.route("/student_dashboard")
def student_dashboard():
    return render_template("student_dashboard.html")


@app.route("/add_book")
def add_book_page():
    return render_template("add_book.html")


@app.route("/add_book", methods=["POST"])
def add_book():

    book_name = request.form["book_name"]
    author = request.form["author"]
    category = request.form["category"]
    quantity = request.form["quantity"]

    cursor.execute(
        "INSERT INTO books (book_name,author,category,quantity) VALUES (%s,%s,%s,%s)",
        (book_name,author,category,quantity)
    )

    db.commit()

    return "Book Added Successfully"

@app.route("/view_books")
def view_books():

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    return render_template("view_books.html", books=books)

@app.route("/issue_book")
def issue_book_page():
    return render_template("issue_book.html")


@app.route("/issue_book", methods=["POST"])
def issue_book():

    student_id = request.form["student_id"]
    book_id = request.form["book_id"]
    issue_date = request.form["issue_date"]

    cursor.execute(
        "INSERT INTO issue_books (student_id, book_id, issue_date)  VALUES (%s,%s,%s)",
        (student_id, book_id, issue_date)
    )

    db.commit()

    return "Book Issued Successfully"

@app.route("/return_book")
def return_book_page():
    return render_template("return_book.html")


@app.route("/return_book", methods=["POST"])
def return_book():

    issue_id = request.form["issue_id"]

    cursor.execute(
        "DELETE FROM issue_books WHERE id=%s",
        (issue_id,)
    )

    db.commit()

    return "Book Returned Successfully"


#for  delete book
@app.route("/delete_book/<int:id>")
def delete_book(id):

    cursor.execute("DELETE FROM books WHERE id=%s", (id,))
    db.commit()

    return redirect("/view_books")



if __name__ == "__main__":
    app.run(debug=True)
