from flask import Flask ,render_template

app=Flask(__name__)

@app.route("/")
def d1():
    return render_template("index.html")

@app.route("/404.html")
def d2():
    return render_template("404.html")

@app.route("/about.html")
def d3():
    return render_template("about.html")

@app.route("/blog.html")
def d4():
    return render_template("blog.html")

@app.route("/book.html")
def d5():
    return render_template("book.html")

@app.route("/contact.html")
def d6():
    return render_template("contact.html")

@app.route("/event.html")
def d7():
    return render_template("event.html")

@app.route("/index.html")
def d8():
    return render_template("index.html")

@app.route("/menu.html")
def d9():
    return render_template("menu.html")

@app.route("/service.html")
def d10():
    return render_template("service.html")

@app.route("/team.html")
def d11():
    return render_template("team.html")

@app.route("/testimonial.html")
def d12():
    return render_template("testimonial.html")

@app.route("/login.html")
def d13():
    return render_template("login.html")

app.run(debug=True)