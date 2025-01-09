from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'studentmanagement'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

try:
    # Sử dụng application context
    with app.app_context():
        conn = mysql.connection  # Kết nối MySQL
        print("Connection is successful!")
        cursor = conn.cursor()

        # Thực thi truy vấn SQL
        cursor.execute("SELECT * FROM student")
        data = cursor.fetchall()
        print("ID\tCode\tName")
        for item in data:
            print(item[0], "\t", item[1], "\t", item[2])

except Exception as e:
    print("Error = ", e)

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("MySQL is closed")
