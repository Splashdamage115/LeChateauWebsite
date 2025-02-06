from flask import Flask, render_template, request, flash, redirect
import DBcm
import os
from dotenv import load_dotenv
import random
import string

def generate_random_password(length=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

load_dotenv('config.env')

host = { 
    "host": os.getenv('DB_HOST', 'localhost'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD'),
    "database": os.getenv('DB_NAME')
    }

newUser = {
    "host":os.getenv('DB_HOST', 'localhost'),
    "user":'newuser',
    "password":generate_random_password(),
    "database":'userdb'
}

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

# Create a new user with a secure password
with DBcm.UseDatabase(host) as cursor:
    sql = "DROP USER IF EXISTS %s@'localhost';"
    cursor.execute(sql, (newUser['user'],))
    
    sql = "CREATE USER %s@'localhost' IDENTIFIED BY %s;"
    cursor.execute(sql, (newUser['user'], newUser['password']))
    
    # Grant necessary privileges to the new user
    sql = f"GRANT INSERT ON {newUser['database']}.* TO %s@'localhost';"
    cursor.execute(sql, (newUser['user'],))
    
    # Flush privileges to apply changes
    cursor.execute("FLUSH PRIVILEGES;")

# Home Page
@app.get("/")
def MainPage():
    with DBcm.UseDatabase(newUser) as cursor:
        address = request.remote_addr
        sql = "INSERT INTO site_log (user_ip) VALUES (%s);"
        cursor.execute(sql, (address,))
        
    return render_template(
        "HomePage.html",
        title = "Home Page"
        )

if __name__ == "__main__":
    app.run(debug=True)