from flask import Flask, render_template, redirect, url_for, request, session
import db_interaction

app = Flask(__name__)
app.secret_key = "veryverysecret"

@app.route('/')
def index_redirect():
    return redirect(url_for("index"))

@app.route('/index')
def index():
    # check if the user is already authenticated
    user_id = session.get("user_id", "")
    authenticated = False
    if user_id != "":
        authenticated = True

    return render_template("index.html", status = authenticated)


@app.route('/login', methods=['POST'])
def login():
    # 1 extract the data from the form
    username = request.form["username"]
    password = request.form["password"]
    # 2 check the extracted data
    user = db_interaction.check_user(username,password)
    # 3 if the data is correct -> show the exam page
    if user is not None:
        session["user_id"] = user[0]
        return redirect(url_for('exams'))
    else:
        return redirect(url_for('login_error'))

@app.route('/login_error')
def login_error():
    return render_template("login_error.html")


@app.route('/exams')
def exams():
    user_id = session.get("user_id","")
    if user_id == "":
        return redirect(url_for("index"))
    else:
        exams = db_interaction.get_all_exams(user_id)
        return render_template("exams.html", user_exams = exams)

@app.route('/logout')
def logout():
    del session["user_id"]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
