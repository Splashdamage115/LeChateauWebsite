from flask import Flask, render_template, flash, redirect
import DBcm

creds = { "host": "localhost", "user": "localuser", "password": "localpasswd", "database": "tempDB" }

app = Flask(__name__)

app.secret_key = "u 03  N UPEW Fj fu9ps J89FE9-37U8 u80se-fsid73jifosdpa872rgy5r3820G7F8W9B23RYU8Q7803ry80Y8vbyt(&vY&b yg g &*G ^y Gg89g Y7)"


# Home Page
@app.get("/")
def MainPage():
    return render_template(
        "HomePage.html",
        title = "Home Page"
        )

if __name__ == "__main__":
    app.run(debug=True)