from flask import Flask
from flask import request, abort, url_for, redirect, session


app = Flask(__name__)

# hello

# @app.route("/")
# def hello():
#     return "Hello World! :("

@app.route("/foo")
def fooController():
    return "<h1>THIS IS THE FOO PAGE</h1>"


@app.route("/bar/")
def bar():
    return "<h1>this is the bar page</h1>"

formpage = """<!DOCTYPE html>
<html>
    <head>
        <title>Basic form</title>
    </head>
    <body>
        <form action="" method="post">
            Enter a number:  <input type="text" name="anumber" />
            <br />
            Enter a string:  <input type="text" name="astring" />
            <br />
            Enter a dog: <input type="text" name="adog" />
            <br />

            <input type="submit" value="submit" />
        </form>
    </body>
</html>
"""

presentpage = """<!DOCTYPE html>
<html>
    <head>
        <title>Present data!</title>
    </head>
    <body>
        You entered this number:  {}
        <br />
        You entered this string:  {}
        <br />
        You entered this dog: {}
    </body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        return presentpage.format(request.form["anumber"], request.form["astring"], request.form["adog"])
    else:
        return formpage
    
users = {"alice": "qwert", "bob": "asdfg", "charlie": "zxcvb"}

loginPage = """<!DOCTYPE html>
<html>
    <head>
        <title>Basic form</title>
    </head>
    <body>
        <form action="" method="post">
            Username:  <input type="text" name="user" />
            <br />
            Password:  <input type="text" name="pass" />
            <br />
            <input type="submit" value="submit" />
        </form>
    </body>
</html>
"""

curProfile = """<!DOCTYPE html>
<html>
    <head>
        <title>Your profile!</title>
    </head>
    <body>
        Welcome back!
        <a href="{}">click here to logout</a>
    </body>
</html>
"""

otherProfile = """<!DOCTYPE html>
<html>
    <head>
        <title>{0}'s profile!</title>
    </head>
    <body>
        This is {0}'s profile page.
    </body>
</html>
"""

logoutPage = """<!DOCTYPE html>
<html>
    <head>
        <title>Logged out</title>
    </head>
    <body>
        You have successfully been logged out!
    </body>
</html>
"""


# by default, direct to login
@app.route("/")
def default():
    return redirect(url_for("login_controller"))


@app.route("/login/", methods=["GET", "POST"])
def login_controller():
    # first check if the user is already logged in
    if "username" in session:
        return redirect(url_for("profile", username=session["username"]))

    # if not, and the incoming request is via POST try to log them in
    elif request.method == "POST":
        if (
            request.form["user"] in users
            and users[request.form["user"]] == request.form["pass"]
        ):
            session["username"] = request.form["user"]
            return redirect(url_for("profile", username=session["username"]))
        abort(401)

    # if all else fails, offer to log them in
    return loginPage


@app.route("/profile/")
@app.route("/profile/<username>")
def profile(username=None):
    if not username:
        # if no profile specified, either:
        #     * direct logged in users to their profile
        #     * direct unlogged in users to the login page
        if "username" in session:
            return redirect(url_for("profile", username=session["username"]))
        else:
            return redirect(url_for("login_controller"))

    elif username in users:
        # if specified, check to handle users looking up their own profile
        if "username" in session and session["username"] == username:
            return curProfile.format(url_for("unlogger"))
        else:
            return otherProfile.format(username)

    else:
        # cant find profile
        abort(404)


@app.route("/logout/")
def unlogger():
    # if logged in, log out, otherwise offer to log in
    if "username" in session:
        # note, here were calling the .clear() method for the python dictionary builtin
        session.clear()
        return logoutPage
    else:
        return redirect(url_for("login_controller"))


# needed to use sessions
# note that this is a terrible secret key
app.secret_key = "this is a terrible secret key"