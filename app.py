
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anushka2003@",  # 🔁 Replace with your MySQL root password
)
cursor = db.cursor()

# Create Database and Table if not exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Employee_DB")
cursor.execute("USE Employee_DB")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee_Registration (
        Serial_No INT PRIMARY KEY AUTO_INCREMENT,
        Employee_Name VARCHAR(100) NOT NULL,
        Designation VARCHAR(100) NOT NULL,
        Department VARCHAR(100) NOT NULL
    )
""")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        designation = request.form['designation']
        department = request.form['department']

        insert_query = "INSERT INTO Employee_Registration (Employee_Name, Designation, Department) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, designation, department))
        db.commit()
        return redirect('/')

    cursor.execute("SELECT * FROM Employee_Registration")
    employees = cursor.fetchall()
    return render_template("index.html", employees=employees)


if __name__ == '__main__':
    app.run(debug=True)
