import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ======================
# MySQL Configuration
# ======================
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'crudapp'
#app.config['MYSQL_PASSWORD'] = 'StrongPass@123'
#app.config['MYSQL_DB'] = 'crud_demo'

app.config['MYSQL_HOST'] = os.getenv("DB_HOST", "localhost")
app.config['MYSQL_USER'] = os.getenv("DB_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASS")
app.config['MYSQL_DB'] = os.getenv("DB_NAME", "crud_demo")

if not app.config['MYSQL_USER'] or not app.config['MYSQL_PASSWORD']:
    raise RuntimeError("Database credentials not set in environment variables")

mysql = MySQL(app)

# ======================
# READ
# ======================
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.close()
    return render_template("index.html", students=students)

# ======================
# CREATE
# ======================
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name,email,course) VALUES (%s,%s,%s)",
                    (name,email,course))
        mysql.connection.commit()
        cur.close()

        flash("Student Added Successfully!")
        return redirect(url_for('index'))

    return render_template("add.html")

# ======================
# UPDATE
# ======================
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_student(id):
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        cur.execute("UPDATE students SET name=%s,email=%s,course=%s WHERE id=%s",
                    (name,email,course,id))
        mysql.connection.commit()
        cur.close()

        flash("Student Updated Successfully!")
        return redirect(url_for('index'))

    cur.execute("SELECT * FROM students WHERE id=%s",[id])
    student = cur.fetchone()
    cur.close()

    return render_template("edit.html", student=student)

# ======================
# DELETE
# ======================
@app.route('/delete/<int:id>')
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s",[id])
    mysql.connection.commit()
    cur.close()

    flash("Student Deleted Successfully!")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
